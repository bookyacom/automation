'use strict';

'use strict';

import Sequelize from 'sequelize';
import assert    from 'assert';

import { sequelizeDB } from '../connection';

const location = sequelizeDB.define('location', {
  name: {
    type: Sequelize.STRING,
    allowNull: false
  },
  unit: Sequelize.STRING,
  street: Sequelize.STRING,
  fullAddress: {
    type: Sequelize.TEXT,
    field: 'full_address'
  },
  region: Sequelize.STRING,
  state: Sequelize.STRING,
  postcode: Sequelize.STRING,
  district: Sequelize.STRING,
  city: Sequelize.STRING,
  provience: Sequelize.STRING,
  country: Sequelize.STRING,
  point: Sequelize.GEOMETRY('Point'),
  pgZone: {
    type: Sequelize.GEOMETRY('Polygon'),
    field: 'pg_zone'
  },
  type: {
    type: Sequelize.ENUM,
    values: ['country', 'poi', 'provience', 'district', 'region', 'city', 'state']
  }
}, {
  createdAt: 'created_at',
  updatedAt: 'updated_at',
  classMethods: {
    createVenue: function(venue) {
      return this.findOrCreate({
        where: {
          name    : venue.name,
          country : venue.country,
          city    : venue.city
        },
        defaults: {
          name    : venue.name,
          country : venue.country,
          city    : venue.city,
          type    : venue.type,
          region  : venue.region,
          point   : Sequelize.fn('ST_GeomFromText', `POINT(${venue.lat} ${venue.lng})`)
        }
      }).spread(function(location, created) {
        location = location.toJSON();
        if (!location) throw new Error('location unable to create');
        return location.id;
      });
    }
  }
});

export default location;
