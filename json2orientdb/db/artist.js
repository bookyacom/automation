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
    featured_track,
    bookya_url
  } = artist;

  if (!cover_photo) cover_photo = profile_photo;

  assert(name && bookya_url, `${name}, ${profile_photo}, ${cover_photo}, should have artist values`);

  let setter = {
    full_name     : name,
    display_name  : name,
    agent_list, genre_list, email, management, manager_email, territories,
    website_list, other_names, nationality, featured_track,
    bookya_url,
    artist_bio,
    record_labels
  };

  if (based_in) {
    setter.based_in = based_in;
  }

  return db
    .update('Artist')
    .set(setter)
    .upsert()
    .return('AFTER')
    .where({
      full_name    : name,
      display_name : name
    })
    .one()
    .then((artist) => {
      // if (artist) return artist['@rid'];
      return artist;
    });
}

export let checkMediaUrl = function(value) {
  return db
    .select('count(*)')
    .from('media')
    .where(`value LIKE '%${value}%'`)
    .scalar()
    .then(count => count > 0);
};

export let updateCoverPhoto = function(id, cover_photo) {
  assert(id);

  return db
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
    .let('updateArtist', (statement) => {
      statement
        .update('Artist')
        .set(`cover_photo=$coverImage[0]`)
        .where({
          '@rid': id
        })
        .return('AFTER');
    })
    .commit()
    .return('$updateArtist')
    .one();
};

export let updateProfilePhoto = function(id, profile_photo) {
  assert(id);

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
    .let('updateArtist', (statement) => {
      statement
        .update('Artist')
        .set(`profile_photo=$profileImage[0]`)
        .where({
          '@rid': id
        })
        .return('AFTER');
    })
    .commit()
    .return('$updateArtist')
    .one();
};

export let checkBookyaUrl = function *({ name }) {
  assert(name);

  let url   = name.toLowerCase().trim().replace(/ /g, '-');
  let count = 1;
  let notFound = true;
  while(notFound) {
    yield db
      .select('count(*)')
      .from('artist')
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
