'use strict';

import assert from 'assert';
import slug from 'slug';

import db from '../connection';

const TABLE_NAME = 'Venue';

export let create = (venue) => {
  let {
    profile_photo,
    name,
    direct_email: email,
    bio,
    websites: website_list,
    genre_list,
    bookya_url,
    contact_person,
    contact_number,
		location_id,
		external_id,
		capacity,
		performance_area_count,
		type_list
  } = venue;

  assert(name && bookya_url, `${name}, ${profile_photo}, should have venue values`);

  let setter = {
    display_name: name,
    genre_list,
    email,
    website_list,
    bookya_url,
    bio,
    contact_person,
    contact_number,
		location_id,
		external_id,
		capacity,
		performance_area_count,
		type_list,
		public: true
  };

  return db
    .update(TABLE_NAME)
    .set(setter)
    .upsert()
    .return('AFTER')
    .where({
      display_name : name
    })
    .one()
    .then(record => {
      return record;
    });
}

export let checkBookyaUrl = function *({ name }) {
  assert(name);

  let url = slug(name);
  let count = 1;
  let notFound = true;
  while(notFound) {
    yield db
      .select('count(*)')
      .from(TABLE_NAME)
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
    .let('updateProfile', (statement) => {
      statement
        .update(TABLE_NAME)
        .set(`cover_photo=$coverImage[0]`)
        .where({
          '@rid': id
        })
        .return('AFTER');
    })
    .commit()
    .return('$updateProfile')
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
    .let('updateProfile', (statement) => {
      statement
        .update(TABLE_NAME)
        .set(`profile_photo=$profileImage[0]`)
        .where({
          '@rid': id
        })
        .return('AFTER');
    })
    .commit()
    .return('$updateProfile')
    .one();
};
