'use strict';

import assert from 'assert';
import slug from 'slug';

import db from '../connection';

const TABLE_NAME = 'Promoter';

export let createPromoter = function(promoter) {
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
    contact_number,
		event_type_list,
		significant_booking_list,
		concept_list,
		event_location_list
  } = promoter;

  assert(name && bookya_url, `${name}, ${profile_photo}, should have promoter values`);

  let setter = {
    display_name  : name,
    full_name  : name,
    genre_list,
    email,
    website_list,
    bookya_url,
    bio,
    contact_person,
    contact_number,
		event_type_list,
		significant_booking_list,
		concept_list,
		event_location_list
  };

  if (based_in) {
    setter.based_in = based_in;
  }

  return db
    .update(TABLE_NAME)
    .set(setter)
    .upsert()
    .return('AFTER')
    .where({
      display_name : name
    })
    .one()
    .then((promoter) => {
      return promoter;
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
    .let('updatePromoter', (statement) => {
      statement
        .update(TABLE_NAME)
        .set(`cover_photo=$coverImage[0]`)
        .where({
          '@rid': id
        })
        .return('AFTER');
    })
    .commit()
    .return('$updatePromoter')
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
    .let('updatePromoter', (statement) => {
      statement
        .update(TABLE_NAME)
        .set(`profile_photo=$profileImage[0]`)
        .where({
          '@rid': id
        })
        .return('AFTER');
    })
    .commit()
    .return('$updatePromoter')
    .one();
};
