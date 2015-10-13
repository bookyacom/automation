'use strict';

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
