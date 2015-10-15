'use strict';

import debug  from 'debug';
import parser from 'csv-parse';
import cli    from 'cli';

const trace  = debug('automation:csv2json:trace');
const error  = debug('automation:csv2json:error');
const stdout = console.log;
const stderr = console.error;

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
  with_youtube_channel : 0,
  genres : {}
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

  return p;
}

function analytics(out) {
  function per(met) {
    return '(' + (met / stats.total_profiles * 100).toFixed(2) + ' %)';
  }

  function tot(met) {
    return ('    ' + met).slice(-4) + '/' + stats.total_profiles + ' ';
  }

  out('TOTAL............................. ' + stats.total_profiles);
  out('---------------------------------------------------------');
  out('with profile photo................ ' + tot(stats.with_profile_photo) + per(stats.with_profile_photo));
  out('with cover photo.................. ' + tot(stats.with_cover_photo) + per(stats.with_cover_photo));
  out('complete for recommendation page.. ' + tot(stats.with_short_info) + per(stats.with_short_info));
  out('complete for featured page........ ' + tot(stats.with_mini_info) + per(stats.with_mini_info));
  out('with contact information.......... ' + tot(stats.with_contact_info) + per(stats.with_contact_info));
  out('---------------------------------------------------------');
  out('social media: BandsInTown......... ' + tot(stats.with_bandsintown) + per(stats.with_bandsintown));
  out('social media: Beatport DJ......... ' + tot(stats.with_beatport_dj) + per(stats.with_beatport_dj));
  out('social media: Beatport Pro........ ' + tot(stats.with_beatport_pro) + per(stats.with_beatport_pro));
  out('social media: Facebook Page....... ' + tot(stats.with_facebook_page) + per(stats.with_facebook_page));
  out('social media: Instagram........... ' + tot(stats.with_instagram_id) + per(stats.with_instagram_id));
  out('social media: iTunes.............. ' + tot(stats.with_itunes_id) + per(stats.with_itunes_id));
  out('social media: LastFM.............. ' + tot(stats.with_lastfm_id) + per(stats.with_lastfm_id));
  out('social media: MixCloud............ ' + tot(stats.with_mixcloud_id) + per(stats.with_mixcloud_id));
  out('social media: PartyFlock.......... ' + tot(stats.with_partyflock) + per(stats.with_partyflock));
  out('social media: SongKick............ ' + tot(stats.with_songkick_id) + per(stats.with_songkick_id));
  out('social media: SoundCloud.......... ' + tot(stats.with_soundlcoud_id) + per(stats.with_soundlcoud_id));
  out('social media: Spotify............. ' + tot(stats.with_spotify_id) + per(stats.with_spotify_id));
  out('social media: Twitter............. ' + tot(stats.with_twitter_id) + per(stats.with_twitter_id));
  out('social media: Youtube............. ' + tot(stats.with_youtube_channel) + per(stats.with_youtube_channel));
  out('---------------------------------------------------------');
  out(genres);
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
    let genres = datum[6].split(',').map((e) => { return e.trim().toLowerCase(); });
    
    genres.forEach(function (genre) {
      stats.genres[genre] = true;
    });

    return p;
  } catch (err) {
    error(err);
    return null;
  }
}

//*****************************************************************************
// Main routine to parse CSV and convert them to JSON 
//*****************************************************************************
function main(csv) {
  let collection = [];

  // Parse a line of CSV and return a JSON
  function parse(data) {
    return new Promise((yes, no) => {
      parser(data, (err, res) => {
        if (err) return no(err);
        yes(res);
      });
    });
  }  

  // Create a collection of promises, each element which contains a promisified
  // parser to convert a line of CSV to a JSON object
  csv.forEach((line) => collection.push(parse(line)));

  Promise.all(collection).then((parsed) => {
    return parsed.map((d) => metric(transform(d.shift()))).filter((e) => (e !== null));
  }).then((res) => {
    stdout(JSON.stringify(res, null, 2));
    analytics(stderr);
  }).catch((err) => {
    stderr(err);
    process.exit(1);
  });
}

//*****************************************************************************
// CLI handling
//*****************************************************************************
cli.withStdinLines((lines, nl) => {
  main(lines);
});