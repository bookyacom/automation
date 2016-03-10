'use strict';

const tos3 = require('tos3');
const co   = require('co');

const s3Base = 'bookya.s3.amazonaws';
const db = require('./db');
const uploader = tos3({
  ACCESS_KEY   : process.env.AWS_ACCESS_KEY || 'AKIAIFAQBRGPOM7P5QMA',
  SECRET_KEY   : process.env.AWS_SECRET_KEY || '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' ,
  BUCKET       : process.env.S3_BUCKET      || 'bookya-dev',
  ACL          : 'public-read'
});

function getMedias() {
  return db
    .select('@rid as id, value')
    .from('Media')
    .where(`not (value LIKE '%${s3Base}%')`)
    .where(`type IN ['profile', 'cover']`)
    .limit(40)
    .all();
}

function getProfilePictures() {
  return db
    .select('@rid as id, profile_photo')
    .from('user')
    .where(`not (profile_photo LIKE '%${s3Base}%')`)
    .where(`profile_photo is not null`)
    .all();
}

function updateMedia(id, value) {
  return db
    .update('Media')
    .where({
      '@rid': id
    })
    .set({
      value
    })
    .scalar();
}

function removeMedia(id) {
  let promises = [];

  promises.push(db
    .update('Artist')
    .set({
      profile_photo: null
    })
    .where({
      profile_photo: id
    })
    .scalar()
  );

  promises.push(db
    .update('Artist')
    .set({
      cover_photo: null
    })
    .where({
      cover_photo: id
    })
    .scalar()
  );

  return Promise.all(promises)
    .then(function() {
      return db
        .delete('vertex', id)
        .scalar();
    });
}

function updateProfile(id, url) {
  return db
    .update('user')
    .where({
      '@rid': id
    })
    .set({
      profile_photo: url
    })
    .scalar();
}

function removeUserProfilePhoto(id) {
  return db
    .update('user')
    .where({
      '@rid': id
    })
    .set({
      profile_photo: null
    })
    .scalar();
}

function upload(url) {
  return uploader(url);
}

function *main() {
  let medias = yield getMedias();
  console.log(medias.length);
  let promises = [];
  let profilesPromises = [];

  while(medias.length > 0) {
    for (let media of medias) {
      let promise = upload(media.value)
      .then((url) => {
        return updateMedia(media.id, url);
      })
      .catch((e) => {
        console.error(e);
        return removeMedia(media.id);
      });
      promises.push(
        promise
      );
    }

    yield Promise.all(promises);
    console.log('next batch');
    promises = [];
    medias = yield getMedias();
    console.log(medias.length);
  }

  // let profiles = yield getProfilePictures();
  // console.log(profiles.length);
  //
  // for (let profile of profiles) {
  //   let promise = upload(profile.profile_photo)
  //     .then((url) => {
  //       console.log(profile.id, url);
  //       return updateProfile(profile.id, url);
  //     })
  //     .catch((err) => {
  //       console.error(err);
  //       console.log(profile.id);
  //       return removeUserProfilePhoto(profile.id);
  //     });
  //
  //   profilesPromises.push(
  //     promise
  //   );
  // }
  //
  // yield Promise.all(profilesPromises);
  return 0;
}

co(function *() {
  return yield main();
})
.then(process.exit.bind(process, 0))
.catch(process.exit.bind(process, 1));
