'use strict';

import aws from 'aws-sdk';
import fileType from 'file-type';
import uuid from 'uuid';
import assert from 'assert';
import got from 'got';

export const uploader = function() {
  const config = {
    ACCESS_KEY   : process.env.AWS_ACCESS_KEY || 'AKIAIPLWSNRY2EJCGAYA',
    SECRET_KEY   : process.env.AWS_SECRET_KEY || '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' ,
    BUCKET       : process.env.S3_BUCKET      || 'bookya-storage',
    ACL          : 'public-read',
    URL          : 'https://bookya-storage.s3.amazonaws.com/'
  };

  aws.config.update({
    accessKeyId: config.ACCESS_KEY,
    secretAccessKey: config.SECRET_KEY
  });

  const s3 = new aws.S3();

  return function(url, name) {
    assert(url && name);

    return new Promise(function(resolve, reject) {
      got(url, {encoding: null})
        .then(res => {
          let chuck = res.body;
          let type = fileType(new Buffer(chuck));

          s3.upload({
            Bucket: config.BUCKET,
            Key: name,
            Body: chuck,
            ContentType: type.mime,
            ACL: config.ACL
          }, function(err, data) {
            if (err) return reject(err);
            resolve(data.Location);
          });
        })
        .catch(reject);
    });
  };
};

export const generateFileName = function() {
  return uuid.v1();
};
