'use strict';

import fs     from 'fs';
import debug  from 'debug';
import parser from 'csv-parse';
import cli    from 'cli';
import util   from 'util';

const trace = debug('automation:csv2json:trace');
const error = debug('automation:csv2json:error');

let stats = {
  total_profiles : 0,
  empty_profiles : 0,
  with_profile_photo : 0,
  with_cover_photo : 0,
  with_short_info : 0,
  with_mini_info : 0,
  with_contact_info : 0,
  with_bandsintown : 0,
  with_beatport_dj : 0,
  with_beatport_pro : 0,
  with_facebook_page : 0,
  with_instagram_id : 0,
  with_itunes_id : 0,
  with_lastfm_id : 0,
  with_mixcloud_id : 0,
  with_partyflock : 0,
  with_songkick_id : 0,
  with_soundlcoud_id : 0,
  with_spotify_id : 0,
  with_twitter_id : 0,
  with_youtube_channel : 0
};

function metric(p) {
  stats.total_profiles++

  (p.profile_photo) ? stats.with_profile_photo++ : null;
  (p.cover_photo) ? stats.with_cover_photo++ : null;
  (p.profile_photo && p.name && p.genres) ? stats.with_short_info++ : null; 
  (p.profile_photo && p.name) ? stats.with_mini_info++ : null;
  (p.email_manager || p.agency.global.email || p.agency.europe.email || p.agency.usa.email || p.direct_email) ? stats.with_contact_info++ : null;
  (p.bandsintown) ? stats.with_bandsintown++ : null;
  (p.beatport_dj_id) ? stats.with_beatport_dj++ : null;
  (p.beatport_pro_id) ? stats.with_beatport_pro++ : null;
  (p.facebook_page) ? stats.with_facebook_page++ : null;
  (p.instagram_id) ? stats.with_instagram_id++ : null;
  (p.itunes_id) ? stats.with_itunes_id++ : null;
  (p.lastfm_id) ? stats.with_lastfm_id++ : null;
  (p.mixcloud_id) ? stats.with_mixcloud_id++ : null;
  (p.partyflock) ? stats.with_partyflock++ : null;
  (p.songkick_id) ? stats.with_songkick_id++ : null;
  (p.soundcloud_id) ? stats.with_soundlcoud_id++ : null;
  (p.spotify_id) ? stats.with_spotify_id++ : null;
  (p.twitter_id) ? stats.with_twitter_id++ : null;
  (p.youtube_channel) ? stats.with_youtube_channel++ : null;

  return Promise.resolve(p);
}

function analytics() {
  function per(met) {
    return '(' + (met / stats.total_profiles * 100).toFixed(2) + ' %)';
  }

  function tot(met) {
    return ('    ' + met).slice(-4) + '/' + stats.total_profiles + ' ';
  }

  console.log('TOTAL............................. ' + stats.total_profiles);
  // console.log('EMPTY............................. ' + stats.empty_profiles + ' ' + per(stats.empty_profiles));
  console.log('---------------------------------------------------------');
  console.log('with profile photo................ ' + tot(stats.with_profile_photo) + per(stats.with_profile_photo));
  console.log('with cover photo.................. ' + tot(stats.with_cover_photo) + per(stats.with_cover_photo));
  console.log('complete for recommendation page.. ' + tot(stats.with_short_info) + per(stats.with_short_info));
  console.log('complete for featured page........ ' + tot(stats.with_mini_info) + per(stats.with_mini_info));
  console.log('with contact information.......... ' + tot(stats.with_contact_info) + per(stats.with_contact_info));
  // console.log('---------------------------------------------------------');
  // console.log('social media: BandsInTown......... ' + tot(with_bandsintown) + per(with_bandsintown));
  // console.log('social media: Beatport DJ......... ' + tot(with_beatport_dj) + per(with_beatport_dj));
  // console.log('social media: Beatport Pro........ ' + tot(with_beatport_pro) + per(with_beatport_pro));
  // console.log('social media: Facebook Page....... ' + tot(with_facebook_page) + per(with_facebook_page));
  // console.log('social media: Instagram........... ' + tot(with_instagram_id) + per(with_instagram_id));
  // console.log('social media: iTunes.............. ' + tot(with_itunes_id) + per(with_itunes_id));
  // console.log('social media: LastFM.............. ' + tot(with_lastfm_id) + per(with_lastfm_id));
  // console.log('social media: MixCloud............ ' + tot(with_mixcloud_id) + per(with_mixcloud_id));
  // console.log('social media: PartyFlock.......... ' + tot(with_partyflock) + per(with_partyflock));
  // console.log('social media: SongKick............ ' + tot(with_songkick_id) + per(with_songkick_id));
  // console.log('social media: SoundCloud.......... ' + tot(with_soundlcoud_id) + per(with_soundlcoud_id));
  // console.log('social media: Spotify............. ' + tot(with_spotify_id) + per(with_spotify_id));
  // console.log('social media: Twitter............. ' + tot(with_twitter_id) + per(with_twitter_id));
  // console.log('social media: Youtube............. ' + tot(with_youtube_channel) + per(with_youtube_channel));
}

function transform(datum) {
  try {
    let p = {
      name : datum[1],
      profile_photo : datum[2],
      cover_photo : datum[3],
      artist_bio : datum[4],
      websites : datum[5],
      genres : datum[6],
      based_in : datum[7],
      nationality : datum[8],
      real_name_1 : datum[9],
      real_name_2 : datum[10],
      real_name_3 : datum[11],
      real_name_4 : datum[12],
      real_name_5 : datum[13],
      real_name_6 : datum[14],
      real_name_7 : datum[15],
      real_name_8 : datum[16],
      real_name_9 : datum[17],
      real_name_10 : datum[18],
      real_name_11 : datum[19],
      real_name_12 : datum[20],
      management : datum[21],
      email_manager : datum[22],
      territories : datum[23],
      agency : {
        global : {
          name : datum[24],
          agent : datum[25],
          email : datum[26],
          number : datum[27],
          territories : datum[28]
        },

        europe : {
          name : datum[29],
          agent : datum[30],
          email : datum[31],
          number : datum[32],
          territories : datum[33]
        },

        usa : {
          name : datum[34],
          agent : datum[35],
          email : datum[36],
          number : datum[37],
        }
      },
      direct_email : datum[38],
      record_labels : datum[39],
      bandsintown : datum[40],
      soundcloud_featured : datum[41],
      beatport_dj_id : datum[42],
      beatport_pro_id : datum[43],
      facebook_page : datum[44],
      instagram_id : datum[45],
      itunes_id : datum[46],
      lastfm_id : datum[47],
      mixcloud_id : datum[48],
      partyflock : datum[49],
      songkick_id : datum[50],
      soundcloud_id : datum[51],
      spotify_id : datum[52],
      twitter_id : datum[53],
      youtube_channel : datum[54]
    };

    // Add genres to the genre list
    

    return p;
  } catch (err) {
    error(err);
    return null;
  }
}

cli.withStdinLines((lines, nl) => {
  let self  = this;
  let collection = [];

  lines.shift();

  function parse(data) {
    return new Promise((yes, no) => {
      parser(data, (err, res) => {
        if (err) return no(err);
        yes(res);
      });
    });
  }

  lines.forEach((line) => collection.push(parse(line)));

  Promise.all(collection).then((parsed) => {
    return parsed
      .map((datum) => {
        let formatted = transform(datum.shift());
        metric(formatted);
        return formatted;
      })
      .filter((e) => (e !== null));
  }).then(function (results) {
    console.log(JSON.stringify(results, null, 2));
    // analytics();
  }).catch(function (err) {
    error(err);
    process.exit(1);
  });
});