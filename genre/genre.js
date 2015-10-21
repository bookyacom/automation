'use strict';

import co      from 'co';
import cli     from 'cli';
import debug   from 'debug';
import cleanup from './cleanup';

const stdout = console.log;
const stderr = console.error;
const trace  = debug('automation:genre:trace');
const error  = debug('automation:genre:error');

let genreCheck = {};

function fix(profile) {
  let genres = profile.genres.split(',');
  let top    = Object.keys(cleanup);
  let fixed  = new Set();
  
  for (let genre of genres) {
    genre = genre.trim().toLowerCase();
    let scheme = cleanup[top[top.indexOf(genre)]];

    if (scheme === undefined || scheme === null) {
      trace('Skipped ' + genre);
      continue;
    }

    for (let genre of Object.keys(scheme)) {
      fixed = fixed.add(genre);
    }
  }

  profile.genres = Array.from(fixed); // convert to plain array and assign to profile

  return profile;
}

//*****************************************************************************
// Main routine to extract genres and analyse them
//*****************************************************************************
function main(profiles) {
  let collection = [];

  if (!Array.isArray(profiles)) {
    stderr('Expecting profiles (from STDIN) to be an array');
    process.exit(1);
  }

  profiles.forEach((profile) => {
    let genres = profile.genres;
    fix(profile);

    if (profile.genres.length > 0) {
      stderr(`Changed ${genres} --------> ${profile.genres.join(', ')}`);
    } else {
      stderr(`Skipped ${profile.name} with genre: (${genres})`);
    }
  });

  stdout(JSON.stringify(profiles, null, 2));
}

//*****************************************************************************
// CLI handling
//*****************************************************************************
cli.withStdin((raw) => {
  let data = null;

  try {
    data = JSON.parse(raw);
  } catch (err) {
    stderr('Failed to parse STDIN data, expecting a JSON');
    stderr(err);
    process.exit(1);
  }

  main(data);
});