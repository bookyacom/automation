'use strict';

import timezoner from 'timezoner';
import moment    from 'moment-timezone';
import debug     from 'debug';
import config    from 'config';

const trace   = debug('trace');
let apiKeys = config.TIMEZONE.API_KEYS;
let count   = 0;

export default function *(time, lat, lng) {
  let keyId = count % 12;
  let key   = apiKeys[keyId];

  trace(key);

  let timezone = yield new Promise(function(resolve, reject) {
    timezoner.getTimeZone(
      lat,
      lng,
      function(err, data) {
        count++;
        trace(err);
        if (err) return reject(err);
        trace(data);
        resolve(data.timeZoneId);
      },
      {
        key: key
      }
    );
  });

  const endDate = moment(time).endOf('day').format('YYYY-MM-DDTHH:mm:ss');

  return {
    start_date : moment.tz(time, timezone).format('YYYY-MM-DD HH:mm:ssZ'),
    end_date   : moment.tz(endDate, timezone).format('YYYY-MM-DD HH:mm:ssZ')
  }
}
