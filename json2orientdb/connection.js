'use strict';

import config    from 'config';
import orientDB  from 'orientjs';
import Sequelize from 'sequelize';
import debug     from 'debug';

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

export const sequelizeDB = new Sequelize(config.POSTGRESQL.DB, config.POSTGRESQL.USERNAME, config.POSTGRESQL.PASSWORD, {
  host: config.POSTGRESQL.HOST,
  port: config.POSTGRESQL.PORT,
  dialect: 'postgres',
  logging: trace,
  pool: {
    max: 5,
    min: 0,
    idle: 10000
  }
});

export default db;
