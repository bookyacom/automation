'use strict';

import db from '../connection';

export let createSocialMetric = function(type, id) {
  return db
    .update('SocialMetric')
    .set({
      type, id
    })
    .upsert()
    .return('AFTER')
    .where({
      type, id
    })
    .one()
    .then(function(social) {
      if (social) return social['@rid'];
      return social;
    });
}
