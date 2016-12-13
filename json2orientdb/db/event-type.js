'use strict';

import db from '../connection';

const TABLE_NAME = 'eventtype';

export let create = function(value) {
  value = value.trim();

  return db
    .update(TABLE_NAME)
    .set({
      value
    })
    .upsert()
    .return('AFTER')
    .where({
      value
    })
    .one()
    .then(function(type) {
      if (type) {
        return type['@rid'];
      }
      return type;
    });
};

export let find = (value) => {
  return db
    .select()
    .from(TABLE_NAME)
    .where(`value.toLowerCase() = "${value}"`)
    .one()
    .then(function(genre) {
      if (genre) {
        return genre['@rid'];
      }
      return genre;
    });
};

export let parseTypes = function(types) {
  if (Array.isArray(types)) {
    return types.map(function(type) {
      return type.toLowerCase();
    });
  }

  return types.split(',').map((type) => type.trim().toLowerCase());
};

export let createAll = function *({ event_type_list: types }) {
  let results = [];

  for (let type of parseTypes(types)) {
    let created = yield this.find(type);
    if (created) results.push(created);
  }

  return results;
};
