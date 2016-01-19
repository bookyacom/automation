'use strict';

import db from '../connection';

export let create = function(value) {
  value = value.trim();

  return db
    .update('Genre')
    .set({
      value
    })
    .upsert()
    .return('AFTER')
    .where({
      value
    })
    .one()
    .then(function(genre) {
      if (genre) {
        return genre['@rid'];
      }
      return genre;
    });
};

export let parseGenre = function(genres) {
  if (Array.isArray(genres)) {
    return genres.map(function(genre) {
      return genre.toLowerCase();
    });
  }

  return genres.split(',').map((genre) => genre.toLowerCase());
};

export let createAll = function *({ genres }) {
  let results = [];

  for (let genre of parseGenre(genres)) {
    let created = yield this.create(genre);
    if (created) results.push(created);
  }

  return results;
};
