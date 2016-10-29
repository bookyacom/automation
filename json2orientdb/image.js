'use strict';

import uuid from 'uuid';
import assert from 'assert';
import tos3 from 'tos3';
import config from 'config';

export const uploader = function() {
  const cfg = config.AWS;
  console.log(cfg);

  const uploader = tos3(cfg);

  return function(url, name) {
    assert(url && name);

    return uploader(url, name);
  };
};

export const generateFileName = function() {
  return uuid.v1();
};
