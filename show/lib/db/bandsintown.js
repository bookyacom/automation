'use strict';

import db from '../connection';

export const getBandsInTown = function() {
  return db
    .select('id, type')
    .from('SocialMetric')
    .where({
      type: 'bandsintown'
    })
    .all()
    .then(function(events) {
      return events.map(({ id }) => {
        return id;
      });
    });
}
