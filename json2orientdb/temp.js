'use strict';





let exec = require('child_process').exec;





let countries = ['france', 'germany', 'italy', 'netherlands','portugal','spain', 'turkey','uk'];
let counter = 0;

function initPush(counter) {
    if (counter >= countries.length) {
        console.log('Exiting crawler');
        return;
    };
    let country = countries[counter];
    console.log(country);
    exec(`more tdraw/${country}.json | iojs index.js`, {maxbuffer: 1024*1024},   function(err, stdout, stderr) {
        if (err) 
           console.log(err);
        console.log(stdout);
        counter += 1;
        initPush(counter);
    })
}

initPush(0);