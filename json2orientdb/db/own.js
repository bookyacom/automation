'use strict';

import assert from 'assert';

import db from '../connection';

export let createEdge = function *(artist, socialmetrics) {
  assert(artist && Array.isArray(socialmetrics));
  for (let social of socialmetrics) {
    let count = yield db.select('count(*)')
      .from('Own')
      .where({
        out : artist,
        in  : social
      })
      .scalar();

    if (count === 0) {
      yield db
        .create('EDGE', 'Own')
        .from(artist)
        .to(social)
        .one();
    }
  }

  return true;
};
