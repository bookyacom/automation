'use strict';

import cli      from 'cli';
import orientjs from 'orientjs';
import co       from 'co';

import * as agentModel  from './db/agent';
import * as metricModel from './db/social-metric';
import * as genreModel  from './db/genre';
import * as ownModel    from './db/own';
import * as artistModel from './db/artist';
import locationModel    from './db/location';
import getLocation      from './location';
import * as image from './image';

/*
  create genres
  create agent
  create locations
  create social metric
  create artist
  create own
 */
let count = 0;
let locationList = {};
const uploader = image.uploader();

cli.withStdin((lines, nl) => {
  console.log(lines);
  let artists = JSON.parse(lines);
  let count   = 0;

  co(function *() {
    for (let artist of artists) {
      if (artist.genres && artist.profile_photo) {
        let genres     = yield genreModel.createAll(artist);
        let agents     = yield agentModel.getAgency(artist);
        let locationId = yield createLocation(artist);

        artist.based_in   = locationId;
        artist.agent_list = agents;
        artist.genre_list = genres;

        console.log(artist.based_in);

        let record   = yield parseArtist(artist);
        let artistId = record['@rid'];

        yield updateMedia(record, artistId, artist);

        let socials       = yield getSocialMedia(artist);
        if (socials.length) {
          yield ownModel.createEdge(artistId, socials);
        }
      } else {
        count++;
      }
    }
  })
  .then(() => {
    console.log(count);
    process.exit(0);
  })
  .catch(function(err) {
    console.error(err);
    process.exit(1);
  });
});

const createLocation = function *({ based_in }) {
  let code = locationList[based_in];

  if (!code) {
    let address = yield getLocation(based_in);
    if (address) {
      try {
        let id = yield locationModel.createBasedLocation(address);
        locationList[based_in] = id;
        return id;
      } catch (e) {
        console.error(e);
        return 0;
      }
    }
    return 0;
  }
  return code;
};

const getSocialMedia = function *(artist) {
  let socialmetric_list = [];
  let testNonAlphaNumeric =/\W/g;
  let keys = ['bandsintown', 'beatport_dj_id', 'beatport_pro_id', 'facebook_page',
    'instagram_id', 'itunes_id', 'lastfm_id', 'mixcloud_id', 'partyflock', 'songkick_id',
    'soundcloud_id', 'spotify_id', 'twitter_id', 'youtube_channel'];

  for (let key of keys) {
    let value = artist[key];
    if (key === 'facebook_page') {
      let reg   = new RegExp(/(?:https?:\/\/)?(?:www\.)?facebook\.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[\w\-]*\/)*?(\/)?([^/?]*)/g);
      let values = reg.exec(value);
      if (values && values.length) {
        value = values.pop();
      }
    }

    if (key === 'youtube_channel') {
      let reg   = new RegExp(/(?:https?:\/\/)?(?:www\.)?youtube\.com\/(?:(?:\w)*#!\/)?(?:channel\/)?(?:[\w\-]*\/)*?(\/)?([^/?]*)/g);
      let values = reg.exec(value);
      if (values && values.length) {
        value = values.pop();
      }
    }

    if (value && value.replace(testNonAlphaNumeric, '')) {
      key = key.replace('_id', '');
      let social = yield metricModel.createSocialMetric(key, value);
      if (social) socialmetric_list.push(social);
    }
  }

  return socialmetric_list;
};

const updateMedia = function *(record, id, artist) {
  function *checkAndUpload(url) {
    let name = image.generateFileName();
    let contain = true;
    while (contain) {
      contain = yield artistModel.checkMediaUrl(name);
    }
    return uploader(url, name);
  }

  if (!record.profile_photo) {
    let url = yield checkAndUpload(artist.profile_photo);
    yield artistModel.updateProfilePhoto(id, url);
  }

  if (!record.cover_photo) {
    artist.cover_photo = artist.cover_photo || artist.profile_photo;

    let url = yield checkAndUpload(artist.cover_photo);
    yield artistModel.updateCoverPhoto(id, url);
  }
};

const parseArtist = function *(artist) {
  artist.other_names = getOtherNames(artist);
  artist.bookya_url  = yield artistModel.checkBookyaUrl(artist);
  return yield artistModel.createArtist(artist);
};

const getOtherNames = function(artist) {
  let key   = 'real_name_';
  let names = [];
  for (let x = 1; x < 13; x++) {
    let name = artist[key + x];
    if (name) {
      names.push(name);
    }
  }

  return names;
};
