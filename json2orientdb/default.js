'use strict';

module.exports = {
  ORIENTDB: {
    HOST: process.env.DB_HOST || '127.0.0.1',
    PORT: process.env.DB_PORT || 2424,
    USERNAME: process.env.DB_USERNAME || 'admin',
    PASSWORD: process.env.DB_PASSWORD || 'admin',
    DB: process.env.DB_NAME || 'test-1',
    ROOT_USERNAME: process.env.ROOT_USERNAME,
    ROOT_PASSWORD: process.env.ROOT_PASSWORD
  },
  POSTGRESQL: {
    DB: process.env.PSQL_DB || 'test',
    USERNAME: process.env.PSQL_USERNAME || 'admin',
    PASSWORD: process.env.PSQL_PASSWORD || 'admin',
    HOST: process.env.PSQL_HOST || 'localhost',
    PORT: process.env.PSQL_PORT || 5432,
  },
  // each serves around 2,500 req/day
  MAPS_APIKEYS: [
    'AIzaSyDDseGYLJ16cRYXIJ2P1uOREHtZTOO6AcQ',
    'AIzaSyBh_74EEhRH4iR9kIRJgGE9lT8bdijxTac',
    'AIzaSyCf2m013zJMvOajC0MMCta4chr9bGyLsls',
    'AIzaSyADK2U4peckf-oxXM2ru6lmebQgc48mL5c'
  ]
}
