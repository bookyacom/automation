'use strict';

import co    from 'co';
import cli   from 'cli';
import debug from 'debug';

const stdout = console.log;
const stderr = console.error;
const trace  = debug('automation:genre:trace');
const error  = debug('automation:genre:error');

let genreCheck = {};

function analyse(profile) {
  let genres = profile.genres.split(',');

  for (let genre of genres) {
    genreCheck[genre.trim().toLowerCase()] = true;
  }
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
    analyse(profile);
  });

  // Sort the genres alphabetically
  let sorted = Object.keys(genreCheck).sort();

  stdout(sorted);
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