'use strict';

import nodeGeocoder from 'node-geocoder';
import config from 'config';

const geocoderProvider = 'google';
const httpAdapter      = 'https';
const keys = config.MAPS_APIKEYS;
let count = 0;

export default function(address) {
  const key = keys[count % keys.length];

  const extra = {
      apiKey: key,
      formatter: null
  };
  const geocoder  = nodeGeocoder(geocoderProvider, httpAdapter, extra);
  return new Promise(function(resolve, reject) {
    count++;
    geocoder.geocode(address, function(err, result) {
      console.log(err);
      if (err) return resolve(null);
      if (!result || !result.length) {
        return resolve(null);
      }

      resolve(result.pop());
    });
  });
}
