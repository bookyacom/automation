'use strict';

import db from '../connection';

export let create = function(value) {
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
  return genres.split(',').map((genre) => genre.toLowerCase());
};

export let createAll = function *({ genres }) {
  let results = [];
  genres = this.parseGenre(genres);

  for (let genre of genres) {
    let created = yield this.create(genre);
    if (created) results.push(created);
  }

  return results;
};
