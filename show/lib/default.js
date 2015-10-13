'use strict';

export default {
  ORIENTDB: {
    HOST: process.env.DB_HOST || '127.0.0.1',
    PORT: process.env.DB_PORT || 2424,
    USERNAME: process.env.DB_USERNAME || 'admin',
    PASSWORD: process.env.DB_PASSWORD || 'admin',
    DB: process.env.DB_NAME || 'test',
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
  BIT: {
    APP_ID: 'barcelona'
  },
  SONGKICK: {
    APP_ID: ''
  },
  TIMEZONE: {
    API_KEYS: [
      // 'AIzaSyClMBT1uqcdq-_g9qzSZrXMN2MO3yktwmI', // api project
      // 'AIzaSyBJQsXtssi4CPL4XLXnpGjSBwfa65ohq0c', // gcal
      'AIzaSyArMzMmcU3GAoF7vqEnOFpNjBbiZRc2zGM', // analytics golang
      'AIzaSyAcc3lywNKbnrXIwjA2YGyfkGi_IGf7Xks', // bookya gmap
      'AIzaSyDQ6XU6S8_cI4SFYzEls-8ThiXNafGFSWk', // bookya youtube
      'AIzaSyDnSvvka4DscU12A3DQWZ4m3ltgusUbMzY', // companion app
      'AIzaSyCBz5UrAuacddiJjp_62UQINAoThpNUycI', // gcm project test
      'AIzaSyCP2xG1hDurzfziMRW1-z4wUMqotGTU_ag', // reach out
      'AIzaSyDtFcXysNlWscz9gdDel9rYlgSiY0GLm3A', // imam muda
      'AIzaSyD5RZBd2ycpbqmzE2clvfPz7ZyjojsJSgY', // yt api
      'AIzaSyB9VkNcgCoe-mGVXgbtxNVayBBp5FDODYM', // timezoner 1
      'AIzaSyDDseGYLJ16cRYXIJ2P1uOREHtZTOO6AcQ', // timezoner 2
      'AIzaSyBh_74EEhRH4iR9kIRJgGE9lT8bdijxTac', // timezoner 3
      'AIzaSyCf2m013zJMvOajC0MMCta4chr9bGyLsls'  // timezoner 4
    ]
  }
}
