'use strict';

import assert from 'assert';

import db from '../connection';

export let createAgent = function({ agent, name, email, number, territories }) {
  let setter = {
    agent, name, email, number, territories
  };

  return db
    .update('Agency')
    .set(setter)
    .upsert()
    .return('AFTER')
    .where(setter)
    .one()
    .then(function(agent) {
      if (agent) {
        return agent['@rid'];
      }
      return agent;
    });
};

export const getAgency = function *({ agency }) {
  let agent_list = [];
  for (let location of Object.keys(agency)) {
    let agent   = agency[location];
    if (agent.name && agent.agent) {
      let created = yield this.createAgent(agent);
      if (created) {
        agent_list.push(created);
      }
    }
  }

  return agent_list;
};

export let createAgency = function(agency) {
  let {
    profile_photo,
    name,
    direct_email: email,
    email_manager: manager_email,
    based_in,
    bio,
    websites: website_list,
    genre_list,
    bookya_url,
    contact_person,
    contact_number
  } = agency;

  assert(name && bookya_url, `${name}, ${profile_photo}, should have agency values`);

  let setter = {
    display_name  : name,
    genre_list,
    email,
    website_list,
    bookya_url,
    bio,
    profile_photo,
    contact_person,
    contact_number
  };

  if (based_in) {
    setter.based_in = based_in;
  }

  return db
    .update('agency')
    .set(setter)
    .upsert()
    .return('AFTER')
    .where({
      display_name : name
    })
    .one()
    .then((agency) => {
      return agency;
    });
}

export let checkBookyaUrl = function *({ name }) {
  assert(name);

  let url   = name.toLowerCase().trim().replace(/ /g, '-');
  let count = 1;
  let notFound = true;
  while(notFound) {
    yield db
      .select('count(*)')
      .from('agency')
      .where({
        bookya_url: url
      })
      .scalar()
      .then(function(count) {
        if (!count) {
          notFound = false;
        } else {
          url = url.concat('-' + count);
          count++;
        }
      });
  }

  return url;
};
