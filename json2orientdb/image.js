'use strict';

import uuid from 'uuid';
import assert from 'assert';
import tos3 from 'tos3';

export const uploader = function() {
  const config = {
    ACCESS_KEY   : process.env.AWS_ACCESS_KEY || 'AKIAIPLWSNRY2EJCGAYA',
    SECRET_KEY   : process.env.AWS_SECRET_KEY || '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' ,
    BUCKET       : process.env.S3_BUCKET      || 'bookya-storage',
    ACL          : 'public-read',
    URL          : 'https://bookya-storage.s3.amazonaws.com/'
  };

  const uploader = tos3(config);

  return function(url, name) {
    assert(url && name);

    return uploader(url, name);
  };
};

export const generateFileName = function() {
  return uuid.v1();
};
