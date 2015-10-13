'use strict';

import bandsintown from 'bandsintown';
import config      from 'config';
import debug       from 'debug';
import template    from 'lodash.template';
import moment      from 'moment';

import timer  from '../timer';
const tmpl  = template('bit_<%= id %>');
const trace = debug('trace');
let   count = 1;

export const getArtistEvent = function *(id) {
  const key   = config.BIT.APP_ID + '-' + count;
  const app   = bandsintown(key);

  trace(id, key);
  let events = yield app.getArtistEventList(id)
    .then(function(events) {
      if (events && events.length) {
        count++;
        return events.map(event => {
          let eventId = tmpl({
            id: event.id
          });

          return {
            id          : eventId,
            name        : event.title,
            start_date  : event.datetime,
            description : event.description || event.title,
            ticket_url  : event.ticket_url,
            bandsintown : id,
            venue       : {
              name : event.venue.name,
              city : event.venue.city,
              region  : event.venue.region,
              country : event.venue.country,
              lat     : event.venue.latitude,
              lng     : event.venue.longitude,
              type    : 'poi'
            },
          }
        });
      }
      return [];
    })
    .catch(function(err) {
      trace(err.body);
      return [];
    });

  for (let event of events) {
    if (event.venue && event.venue.lat && event.venue.lng) {
      let dates = yield timer(event.start_date, event.venue.lat, event.venue.lng);
      event.start_date = dates.start_date;
      event.end_date   = dates.end_date;
    }
  }

  return events;
};
