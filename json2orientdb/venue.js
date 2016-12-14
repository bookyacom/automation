'use strict';

import cli      from 'cli';
import orientjs from 'orientjs';
import co       from 'co';

import * as metricModel from './db/social-metric';
import locationModel from './db/location';
import getLocation from './location';
import * as genreModel  from './db/genre';
import * as venueTypeModel  from './db/venue-type';
import * as ownModel from './db/own';
import * as artistModel from './db/artist';
import * as image from './image';
import * as venueModel from './db/venue';
import * as awardModel from './db/award';

let count = 0;
let locationList = {};
const uploader = image.uploader();

cli.withStdin((lines, nl) => {
  const venues = JSON.parse(lines);
  let count   = 0;

  co(function *() {
    for (let venue of venues) {
      if (venue.genres) {
        const genres = yield genreModel.createAll(venue);
				const typeList = yield venueTypeModel.createAll(venue);
        const locationId = yield createLocation(venue);

        venue.location_id = locationId;
				venue.type_list = typeList;
        venue.genre_list = genres;

        const record = yield parseVenue(venue);
        const venueID = record['@rid'];

        yield updateMedia(record, venueID, venue);

        const socials = yield getSocialMedia(venue);
        if (socials.length) {
          yield ownModel.createEdge(venueID, socials);
        }

				// update awards
				yield awardModel.updateAwarded(venue, venueID);
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

function * createLocation({based_in}) {
  let code = locationList[based_in];

  if (!code) {
    code = 0;
    let address = yield getLocation(based_in);
    if (address) {
      try {
        code = yield locationModel.createBasedLocation(address);
        if (code) {
          locationList[based_in] = code;
        } else {
          code = 0;
        }
      } catch (e) {
        console.error(e);
        return 0;
      }
    }
  }
  return code;
};

function * parseVenue(record) {
  record.bookya_url = yield venueModel.checkBookyaUrl(record);
  return yield venueModel.create(record);
}

function * updateMedia(record, id, profile) {
  function *checkAndUpload(url) {
    let name = image.generateFileName();
    let contain = true;
    while (contain) {
      contain = yield artistModel.checkMediaUrl(name);
    }
    let result = null
    try {
      result = yield uploader(url, name);
    } catch (e) {
      console.log(e);
    }

    return result;
  }

  if (!record.profile_photo && profile.profile_photo) {
    let url = yield checkAndUpload(profile.profile_photo);
    if (url) {
      yield venueModel.updateProfilePhoto(id, url);
    }
  }
};

function * getSocialMedia(artist) {
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
