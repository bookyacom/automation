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
import getLocation      from './location'

/*
  create genres
  create agent
  create locations
  create social metric
  create artist
  create own
 */
let count = 0;
cli.withStdin((lines, nl) => {
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

        let artistId      = yield parseArtist(artist);
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
  let address = yield getLocation(based_in);
  if (address) {
    try {
      return yield locationModel.createBasedLocation(address);
    } catch (e) {
      return "";
    }
  }
  return "";
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

    if (value && value.replace(testNonAlphaNumeric, '')) {
      key = key.replace('_id', '');
      let social = yield metricModel.createSocialMetric(key, value);
      if (social) socialmetric_list.push(social);
    }
  }

  return socialmetric_list;
};

const parseArtist = function *(artist) {
  artist.other_names = getOtherNames(artist);
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
