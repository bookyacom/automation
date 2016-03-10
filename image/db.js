'use strict';

const config   =  require('config');
const orientDB =  require('orientjs');
const debug    =  require('debug');

const trace  = debug('trace');
const server = orientDB({
  host: config.ORIENTDB.HOST,
  port: config.ORIENTDB.PORT
});

const db = server.use({
  name: config.ORIENTDB.DB,
  username: config.ORIENTDB.USERNAME,
  password: config.ORIENTDB.PASSWORD
});

db.on('beginQuery', trace);

module.exports = db;
