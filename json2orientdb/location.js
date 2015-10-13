'use strict';

import nodeGeocoder from 'node-geocoder';

const geocoderProvider = 'google';
const httpAdapter      = 'https';
const extra = {
    apiKey: 'AIzaSyDkIuffj3ers2Z5GgGDbGzy57yJy7KmW9I',
    formatter: null
};
const geocoder  = nodeGeocoder(geocoderProvider, httpAdapter, extra);

export default function(address) {
  return new Promise(function(resolve, reject) {
    geocoder.geocode(address, function(err, result) {
      if (err) return resolve(null);
      if (!result || !result.length) {
        return resolve(null);
      }

      resolve(result.pop());
    });
  });
}
