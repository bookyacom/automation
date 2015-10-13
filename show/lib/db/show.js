'use strict';

import debug from 'debug';

import db from '../connection';

const trace = debug('trace');
const DATE_FORMAT = "yyyy-MM-dd HH:mm:ssX";

export const createShow = function({ id, start_date, end_date, name, description, ticket_url, held_at }) {
  return db
    .update('show')
    .set({
      name,
      description,
      ticket_url,
      held_at,
      id,
      state: 'published'
    })
    .set(`start_date=date("${start_date}", "${DATE_FORMAT}")`)
    .set(`end_date=date("${end_date}", "${DATE_FORMAT}")`)
    .where({
      id
    })
    .upsert()
    .return('AFTER')
    .one();
};

export const createArtistRelation = function({ show, bandsintown }) {
  let social = db
    .select('@rid')
    .from('socialmetric')
    .where({
      id   : bandsintown,
      type : 'bandsintown'
    });

  let artist = db
    .select()
    .from('artist')
    .where(`out('own') in (${social})`);

  return db
    .create('edge', 'performedat')
    .from(artist)
    .to(show)
    .all();
};
