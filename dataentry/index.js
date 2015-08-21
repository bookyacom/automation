'use strict';

require('babel/register');

const fs     = require('fs');
const debug  = require('debug');
const parser = require('csv-parse');
const error  = debug('automation:dataentry:error');
const info   = debug('automation:dataentry:info');

const IN = process.env.IN || './test.csv';
const OUT = process.env.OUT || './out.json';
const WRITE = process.env.WRITE === 1 || false;

function read(filepath) {
  return new Promise(function (resolve, reject) {
    fs.readFile(filepath, 'utf8', function (err, data) {
      if (err) return reject(err);
      resolve(data);
    });
  });
}

function write(filepath, data) {
  return new Promise(function (resolve, reject) {
    let jsonified = JSON.stringify(data, null, 2);
    fs.writeFile(filepath, jsonified, 'utf8', function (err) {
      if (err) return reject(err);
      resolve(jsonified);
    });
  });
}

function parse(data) {
  return new Promise(function (resolve, reject) {
    parser(data, function (err, results) {
      if (err) return reject(err);
      resolve(results);
    });
  });
}

function csv() {
  return read(IN)
    .then(function (data) {
      return parse(data);
    })
    .then(function (results) {
      return transform(results);
    });
}

function transform(results) {
  results.shift(); // remove the header column

  // collect metrics of the results
  let total_profiles       = 0; // total number of profiles
  let empty_profiles       = 0; // total number of empty profiles
  let with_profile_photo   = 0; // profiles with profile photos
  let with_cover_photo     = 0; // profiles with cover photos
  let with_short_info      = 0; // profiles ready to be shown on the recommended page
  let with_mini_info       = 0; // profiles ready to be shown on the featured page
  let with_contact_info    = 0; // profiles that has direct email, manager or agency contact
  let with_bandsintown     = 0;
  let with_beatport_dj     = 0;
  let with_beatport_pro    = 0;
  let with_facebook_page   = 0;
  let with_instagram_id    = 0;
  let with_itunes_id       = 0;
  let with_lastfm_id       = 0;
  let with_mixcloud_id     = 0;
  let with_partyflock      = 0;
  let with_songkick_id     = 0;
  let with_soundlcoud_id   = 0;
  let with_spotify_id      = 0;
  let with_twitter_id      = 0;
  let with_youtube_channel = 0;

  results = results.map(function (arr) {
    let p = {};

    try {
      p = {
        name : arr[1],
        profile_photo : arr[2],
        cover_photo : arr[3],
        artist_bio : arr[4],
        websites : arr[5],
        genres : arr[6],
        based_in : arr[7],
        nationality : arr[8],
        real_name_1 : arr[9],
        real_name_2 : arr[10],
        real_name_3 : arr[11],
        real_name_4 : arr[12],
        real_name_5 : arr[13],
        real_name_6 : arr[14],
        management : arr[15],
        email_manager : arr[16],
        territories : arr[17],
        agency : {
          global : {
            name : arr[18],
            agent : arr[19],
            email : arr[20],
            number : arr[21],
            territories : arr[22]
          },

          europe : {
            name : arr[23],
            agent : arr[24],
            email : arr[25],
            number : arr[26],
            territories : arr[27]
          },

          usa : {
            name : arr[28],
            agent : arr[29],
            email : arr[30],
            number : arr[31],
          }
        },
        direct_email : arr[32],
        record_labels : arr[33],
        bandsintown : arr[34],
        soundcloud_featured : arr[35],
        beatport_dj_id : arr[36],
        beatport_pro_id : arr[37],
        facebook_page : arr[38],
        instagram_id : arr[39],
        itunes_id : arr[40],
        lastfm_id : arr[41],
        mixcloud_id : arr[42],
        partyflock : arr[43],
        songkick_id : arr[44],
        soundcloud_id : arr[45],
        spotify_id : arr[46],
        twitter_id : arr[47],
        youtube_channel : arr[48]
      };

      // increment the total number of profiles
      total_profiles++

      (p.profile_photo) ? with_profile_photo++ : null;
      (p.cover_photo) ?  with_cover_photo++ : null;
      (p.profile_photo && p.name && p.genres) ? with_short_info++ : null; 
      (p.profile_photo && p.name) ? with_mini_info++ : null;
      (p.email_manager || p.agency.global.email || p.agency.europe.email || p.agency.usa.email || p.direct_email) ? with_contact_info++ : null;
      (p.bandsintown) ? with_bandsintown++ : null;
      (p.beatport_dj_id) ? with_beatport_dj++ : null;
      (p.beatport_pro_id) ? with_beatport_pro++ : null;
      (p.facebook_page) ? with_facebook_page++ : null;
      (p.instagram_id) ? with_instagram_id++ : null;
      (p.itunes_id) ? with_itunes_id++ : null;
      (p.lastfm_id) ? with_lastfm_id++ : null;
      (p.mixcloud_id) ? with_mixcloud_id++ : null;
      (p.partyflock) ? with_partyflock++ : null;
      (p.songkick_id) ? with_songkick_id++ : null;
      (p.soundcloud_id) ? with_soundlcoud_id++ : null;
      (p.spotify_id) ? with_spotify_id++ : null;
      (p.twitter_id) ? with_twitter_id++ : null;
      (p.youtube_channel) ? with_youtube_channel++ : null;

      // Check for empty profiles
      let filtered = arr.filter(function (data) {
        if (data) return true;
        return false;
      });

      (filtered.length < 3) ? empty_profiles++ : null;

      return p;
    } catch (err) {
      error(err);
    }

    return null;
  });

  function per(met) {
    return '(' + (met / total_profiles * 100).toFixed(2) + ' %)';
  }

  function tot(met) {
    return ('    ' + met).slice(-4) + '/' + total_profiles + ' ';
  }

  console.log('TOTAL............................. ' + total_profiles);
  console.log('EMPTY............................. ' + empty_profiles + ' ' + per(empty_profiles));
  console.log('---------------------------------------------------------');
  console.log('with profile photo................ ' + tot(with_profile_photo) + per(with_profile_photo));
  console.log('with cover photo.................. ' + tot(with_cover_photo) + per(with_cover_photo));
  console.log('complete for recommendation page.. ' + tot(with_short_info) + per(with_short_info));
  console.log('complete for featured page........ ' + tot(with_mini_info) + per(with_mini_info));
  console.log('with contact information.......... ' + tot(with_contact_info) + per(with_contact_info));
  console.log('---------------------------------------------------------');
  console.log('social media: BandsInTown......... ' + tot(with_bandsintown) + per(with_bandsintown));
  console.log('social media: Beatport DJ......... ' + tot(with_beatport_dj) + per(with_beatport_dj));
  console.log('social media: Beatport Pro........ ' + tot(with_beatport_pro) + per(with_beatport_pro));
  console.log('social media: Facebook Page....... ' + tot(with_facebook_page) + per(with_facebook_page));
  console.log('social media: Instagram........... ' + tot(with_instagram_id) + per(with_instagram_id));
  console.log('social media: iTunes.............. ' + tot(with_itunes_id) + per(with_itunes_id));
  console.log('social media: LastFM.............. ' + tot(with_lastfm_id) + per(with_lastfm_id));
  console.log('social media: MixCloud............ ' + tot(with_mixcloud_id) + per(with_mixcloud_id));
  console.log('social media: PartyFlock.......... ' + tot(with_partyflock) + per(with_partyflock));
  console.log('social media: SongKick............ ' + tot(with_songkick_id) + per(with_songkick_id));
  console.log('social media: SoundCloud.......... ' + tot(with_soundlcoud_id) + per(with_soundlcoud_id));
  console.log('social media: Spotify............. ' + tot(with_spotify_id) + per(with_spotify_id));
  console.log('social media: Twitter............. ' + tot(with_twitter_id) + per(with_twitter_id));
  console.log('social media: Youtube............. ' + tot(with_youtube_channel) + per(with_youtube_channel));

  return results;
}

csv().then(function (results) {
  return write(OUT, results);
}).catch(function (err) {
  error(err);
});