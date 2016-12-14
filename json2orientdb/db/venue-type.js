'use strict';

import db from '../connection';

export let create = function(value) {
  value = value.trim();

  return db
    .update('VenueType')
    .set({
      value
    })
    .upsert()
    .return('AFTER')
    .where({
      value
    })
    .one()
    .then(type => {
      if (type) {
        return type['@rid'];
      }
      return type;
    });
};

export let find = (value) => {
  return db
    .select()
    .from('VenueType')
    .where(`value.toLowerCase() = "${value}"`)
    .one()
    .then(type => {
      if (type) {
        return type['@rid'];
      }
      return type;
    });
};

export let parseVenueTypes = (types) => {
  if (Array.isArray(types)) {
    return types.map(type => {
      return type.toLowerCase();
    });
  }

  return types.split(',').map(type => type.trim().toLowerCase());
};

export let createAll = function *({ type_list }) {
  const results = [];

  for (let type of parseVenueTypes(type_list)) {
    let created = yield this.find(type);
    if (created) results.push(created);
  }

  return results;
};
