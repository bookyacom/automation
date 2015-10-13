'use strict';

import db from './connection';

export const getSocialMetric = function(cb) {
  db.liveQuery(`live select from socialmetric where type IN ['songkick', 'bandsintown']`)
    .on('live-insert', function(data) {
      let content = data.content;
      cb(null, content);
    });
};

export const getSongkick = function(cb) {
  db.liveQuery(`live select from socialmetric where type = 'songkick'`)
    .on('live-insert', function(data) {
      let content = data.content;
      cb(null, content);
    });
};

export const getBandsInTown = function(cb) {
  db.liveQuery(`live select from socialmetric where type = 'bandsintown'`)
    .on('live-insert', function(data) {
      let content = data.content;
      cb(null, content);
    });
};
