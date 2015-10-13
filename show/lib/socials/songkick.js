'use strict';

import Songkick from 'songkick-wrapper';
import config   from 'config';

const app = Songkick.create(config.SONGKICK.APP_ID);

export const getArtistEvent = function(id) {
  return app.getArtistUpcomingEvents(id)
    .then(({ results: events }) => {
      return events;
    });
};
