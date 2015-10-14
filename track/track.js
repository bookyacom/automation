'use strict';

import request from 'request';
import qs      from 'querystring';
import debug   from 'debug';

const trace  = debug('automation:track:trace');
const error  = debug('automation:track:error');
const stderr = console.err;
const stdout = console.log;
const SCID   = '62d2dd20dd7849715a5dc9b200e7df47';

function getFeaturedTrack(profile) {
  // Promisified request module
  function req(url) {
    return new Promise((yes, no) => {
      let apiurl = url + '?' + qs.stringify(params);
      trace(apiurl);
      request.get(apiurl, function (err, res, body) {
        if (err) return no(err);
        yes(res);
      });
    });
  }

  let params = { client_id : SCID, order_by : 'favoritings_count', limit : 1 };
  let userId = profile.soundcloud_id;

  // Ignore if no soundcloudID
  if (!userId) {
    profile.featured_track = '';
    return Promise.resolve(profile);
  }

  return req('https://api.soundcloud.com/users/' + userId + '/tracks')
    .then((res) => {
      let tracks = JSON.parse(res.body);

      profile.featured_track = '';

      if (!Array.isArray(tracks)) {
        return Promise.resolve(profile);
      }

      let featured = tracks.shift();

      if (featured) {
        profile.featured_track = featured.id;
        stats.with_featured_track++;
      }

      return Promise.resolve(profile);
    });
}

//*****************************************************************************
// Main routine to get featured track for each profile that contains a
// soundcloud ID
//*****************************************************************************
function main(profiles) {
  co(function *() {
    let collection = [];

    for (let profile of profiles) {
      try {
        let completed = yield getFeaturedTrack(profile);
        collection.push(completed);
      } catch (err) {
        error('Skipped ' + profile.name + '...');
        error(err);
      }
    }

    return collection;
  }).then((res) => {
    stdout(JSON.stringify(res));
  }).catch((err) => {
    stderr(err);
    process.exit(1);
  });
}

//*****************************************************************************
// CLI handling
//*****************************************************************************
cli.withStdin((data) => {
  let profiles = null;

  try {
    profiles = JSON.parse(data);
  } catch (err) {
    stderr('Failed to parse STDIN data, expecting a JSON');
    stderr(err);
    process.exit(1);
  }

  main(profiles);
});