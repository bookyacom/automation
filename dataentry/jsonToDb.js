'use strict'

require('babel-register');
const fs = require('fs');
const GoogleMapsAPI = require("googlemaps");
const _ = require('lodash')



let googleAPIKey = "AIzaSyC-WSYj5HawYzpBrQRsqRYIf-WXnco8kho";
let publicConfig = {
  key: googleAPIKey,
  stagger_time: 1000, // for elevationPath
  encode_polylines: false,
  secure: true, // use https
};
let gmAPI = new GoogleMapsAPI(publicConfig);


// var res;
// gmAPI.geocode(geocodeParams, function(err, result) {
//   res = result;
//   console.log(result);
// });


function fileReadPromise(filePath) {
  return new Promise(function(resolve, reject) {
    fs.readFile(filePath, "utf8", function(err, data) {
      if (err)
        reject(err);
      var arr = JSON.parse(data);
      resolve(arr);
    });
  })
}

fileReadPromise('out.json').then(function(data) {
  for (let index in data) {
    let aritst = data[index];
    if (!_.isEmpty(aritst.profile_photo) && _.isEmpty(aritst.based_in)) {
      console.log(aritst);
      console.log();
    }
  }
}).catch(function(err) {
  console.log(err)
})
