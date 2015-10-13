'use strict';

import assert from 'assert';

import db from '../connection';

export let createArtist = function(artist) {
  let {
    profile_photo,
    cover_photo,
    nationality,
    name,
    direct_email: email,
    management,
    email_manager: manager_email,
    territories,
    based_in,
    artist_bio,
    websites: website_list,
    other_names,
    agent_list,
    genre_list,
    record_labels,
    featured_track
  } = artist;

  if (!cover_photo) cover_photo = profile_photo;

  assert(name && profile_photo && cover_photo, `${name}, ${profile_photo}, ${cover_photo}, should have artist values`);

  return db
    .let('profileImage', (statement) => {
      let setter = {
        value : profile_photo,
        type  : 'profile'
      };

      statement
        .update('media')
        .set(setter)
        .upsert()
        .return('AFTER')
        .where(setter);
    })
    .let('coverImage', (statement) => {
      let setter = {
        value : cover_photo,
        type  : 'cover'
      };

      statement
        .update('media')
        .set(setter)
        .upsert()
        .return('AFTER')
        .where(setter);
    })
    .let('artist', (statement) => {
      statement
        .update('Artist')
        .set({
          full_name     : name,
          display_name  : name,
          agent_list, genre_list, email, management, manager_email, territories,
          artist_bio, website_list, other_names, nationality, based_in,
          featured_track
        })
        .set(`profile_photo=$profileImage[0]`)
        .set(`cover_photo=$coverImage[0]`)
        .upsert()
        .return('AFTER')
        .where({
          full_name    : name,
          display_name : name
        });
    })
    .commit()
    .return('$artist')
    .one()
    .then((artist) => {
      if (artist) return artist['@rid'];
      return artist;
    });
}
