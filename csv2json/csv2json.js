'use strict';

import debug  from 'debug';
import parser from 'csv-parse';
import cli    from 'cli';
import config from './config';

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
  with_youtube_channel : 0
};

function getFacebookPageID(val) {
  if (!val) {
    return val;
  }

  const matches = val.match(/(?:https?:\/\/)?(?:www\.)?facebook\.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[\w\-]*\/)*?(\/)?([^/?]*)/);
  if (matches) {
    return matches.pop();
  }
  return val;
}

function getInstagramID(val) {
  if (!val) {
    return val;
  }

  const matches = val.match(/(?:https?:\/\/)?(?:www\.)?instagram\.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[\w\-]*\/)*?(\/)?([^/?]*)/);
  if (matches) {
    return matches.pop();
  }
  return val;
}

function getTwitterID(val) {
  if (!val) {
    return val;
  }

  const matches = val.match(/(?:https?:\/\/)?(?:www\.)?twitter\.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[\w\-]*\/)*?(\/)?([^/?]*)/);
  if (matches) {
    return matches.pop();
  }
  return val;
}

function getSouncloudID(val) {
  if (!val) {
    return val;
  }

  const matches = val.match(/(?:https?:\/\/)?(?:www\.)?soundcloud\.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[\w\-]*\/)*?(\/)?([^/?]*)/);
  if (matches) {
    return matches.pop();
  }
  return val;
}

function getYoutubeID(val) {
  if (!val) {
    return val;
  }

  const matches = val.match(/(?:https?:\/\/)?(?:www\.)?youtube\.com\/(?:(?:\w)*#!\/)?(?:channel\/)?(?:[\w\-]*\/)*?(\/)?([^/?]*)/);
  if (matches) {
    return matches.pop();
  }
  return val;
}

function metric(p) {
  if (!p) {
    return p;
  }

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
}

function transform(datum) {
  try {
    const contact = datum[config.CONTACT_NUMBER];

    let p = {
      name : datum[config.NAME],
      profile_photo : datum[config.PROFILE_PHOTO],
      cover_photo : datum[config.COVER_PHOTO],
      bio : datum[config.BIO],
      websites : datum[config.WEBSITE],
      genres : datum[config.GENRES],
      based_in : datum[config.BASED_IN],
      nationality : datum[config.NATIONALITY],
      real_name_1 : datum[config.REAL_NAME || config.NAME],
      management : datum[config.MANAGEMENT],
      email_manager : datum[config.EMAIL_MANAGER || config.EMAIL],
      territories : datum[config.TERRITORIES],
      has_profile: datum[config.BOOKYA_PROFILE] === 'Yes',
      contact_person: datum[config.CONTACT_PERSON],
      contact_number: contact ? contact.trim() : contact,
      agency : {
        global : {
          name : datum[24] || datum[60],
          agent : datum[25] || datum[60],
          email : datum[26] || datum[61],
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
      direct_email : datum[config.EMAIL],
      record_labels : datum[config.RECORD_LABELS],
      bandsintown : datum[config.BANDSINTOWN],
      soundcloud_featured : datum[config.SOUNDCLOUD_FEATURED],
      beatport_dj_id : datum[config.BEATPORT_DJ_ID],
      beatport_pro_id : datum[config.BEATPORT_PRO_ID],
      facebook_page : getFacebookPageID(datum[config.FACEBOOK_PAGE]),
      instagram_id : getInstagramID(datum[config.INSTAGRAM_ID]),
      itunes_id : datum[config.ITUNES_ID],
      lastfm_id : datum[config.LASTFM_ID],
      mixcloud_id : datum[config.MIXCLOUD_ID],
      partyflock : datum[config.PARTYFLOCK],
      songkick_id : datum[config.SONGKICK_ID],
      soundcloud_id : getSouncloudID(datum[config.SOUNDCLOUD_ID]),
      spotify_id : datum[config.SPOTIFY_ID],
      twitter_id : getTwitterID(datum[config.TWITTER_ID]),
      youtube_channel : getYoutubeID(datum[config.YOUTUBE_CHANNEL]),

      // Additional stuff from KL
      press_contact : datum[config.PRESS_CONTACT]
    };

    stderr(`Done with ${p.name}`);

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
        if (err) {
          stderr(data);
          return no(err);
        }
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
