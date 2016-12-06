'use strict';

// module.exports = {
//   ORIENTDB: {
//     HOST: process.env.DB_HOST || '192.168.50.4',
//     PORT: process.env.DB_PORT || 2424,
//     USERNAME: process.env.DB_USERNAME || 'bookya_api',
//     PASSWORD: process.env.DB_PASSWORD || 'FpMOuFq5G9tBwg2Yit89',
//     DB: process.env.DB_NAME || 'bookya_api',
//     ROOT_USERNAME: process.env.ROOT_USERNAME,
//     ROOT_PASSWORD: process.env.ROOT_PASSWORD
//   },
//   POSTGRESQL: {
//     DB: process.env.PSQL_DB || 'test',
//     USERNAME: process.env.PSQL_USERNAME || 'admin',
//     PASSWORD: process.env.PSQL_PASSWORD || 'admin',
//     HOST: process.env.PSQL_HOST || '192.168.50.4',
//     PORT: process.env.PSQL_PORT || 5432,
//   },
//   // each serves around 2,500 req/day
//   MAPS_APIKEYS: [
//     'AIzaSyDDseGYLJ16cRYXIJ2P1uOREHtZTOO6AcQ',
//     'AIzaSyBh_74EEhRH4iR9kIRJgGE9lT8bdijxTac',
//     'AIzaSyCf2m013zJMvOajC0MMCta4chr9bGyLsls',
//     'AIzaSyADK2U4peckf-oxXM2ru6lmebQgc48mL5c'
//   ],
//   AWS: {
//     ACCESS_KEY   : process.env.AWS_ACCESS_KEY || "AKIAIPLWSNRY2EJCGAYA",
//     SECRET_KEY   : process.env.AWS_SECRET_KEY || "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" ,
//     BUCKET       : process.env.S3_BUCKET      || "bookya-storage",
//     EXPIRY_LIMIT : 60,
//     ACL    : 'public-read',
//     URL          : 'https://bookya-storage.s3.amazonaws.com/'
//   }
// }

module.exports = {
  ORIENTDB: {
    HOST: process.env.DB_HOST || 'localhost',
    PORT: process.env.DB_PORT || 2424,
    USERNAME: process.env.DB_USERNAME || 'bookya_api',
    PASSWORD: process.env.DB_PASSWORD || 'FpMOuFq5G9tBwg2Yit89',
    DB: process.env.DB_NAME || 'bookya_api',
    ROOT_USERNAME: process.env.ROOT_USERNAME,
    ROOT_PASSWORD: process.env.ROOT_PASSWORD
  },
  POSTGRESQL: {
    DB: process.env.PSQL_DB || 'bookya_api',
    USERNAME: process.env.PSQL_USERNAME || 'bookya_api',
    PASSWORD: process.env.PSQL_PASSWORD || '5BStISTLnmQIHEIJ1J1H',
    HOST: process.env.PSQL_HOST || 'localhost',
    PORT: process.env.PSQL_PORT || 5432,
  },
  // each serves around 2,500 req/day
  MAPS_APIKEYS: [
    'AIzaSyDDseGYLJ16cRYXIJ2P1uOREHtZTOO6AcQ',
    'AIzaSyBh_74EEhRH4iR9kIRJgGE9lT8bdijxTac',
    'AIzaSyCf2m013zJMvOajC0MMCta4chr9bGyLsls',
    'AIzaSyADK2U4peckf-oxXM2ru6lmebQgc48mL5c'
  ],
  AWS: {
    ACCESS_KEY   : process.env.AWS_ACCESS_KEY || "AKIAIPLWSNRY2EJCGAYA",
    SECRET_KEY   : process.env.AWS_SECRET_KEY || "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" ,
    BUCKET       : process.env.S3_BUCKET      || "bookya-storage",
    EXPIRY_LIMIT : 60,
    ACL    : 'public-read',
    URL          : 'https://bookya-storage.s3.amazonaws.com/'
  }
}
