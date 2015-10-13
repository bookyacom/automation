'use strict';

import co from 'co';
import debug from 'debug';

import { getArtistEvent } from './socials/bandsintown';
import { getBandsInTown } from './db/bandsintown';
import location       from './db/location';
import * as showModel from './db/show';

const trace = debug('trace');

function *main() {
  let allEvents = [];
  let ids = yield getBandsInTown();

  trace(ids);

  for (let id of ids) {
    let events = yield getArtistEvent(id);
    allEvents  = allEvents.concat(events);
  }

  trace(allEvents.length);

  for (let show of allEvents) {
    if (show.venue) {
      let venueId = yield location.createVenue(show.venue);
      trace(venueId);
      show.held_at = venueId;
    }

    let created = yield showModel.createShow(show);
    try {
      yield showModel.createArtistRelation({ bandsintown: show.bandsintown, show: created['@rid'] });
    } catch(e) {
      trace(e);
    }
  }

  return allEvents;
}

co(function *() {
  return yield main();
})
.then(function(events) {
  trace('success...', events.length);
  process.exit(0);
})
.catch(function(err) {
  trace(err);
  process.exit(1);
});
