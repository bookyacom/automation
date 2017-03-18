# automation [![Dependency Status](https://gemnasium.com/badges/4fb0d3a6d4a883ba5ba81cb7aed21741.svg)](https://gemnasium.com/github.com/bookyacom/automation)

Automated scripts repository

## Modules

### extracter

The `extracter` module connects to a Google Sheet and streams the lines into STDOUT in the form of comma separated CSV.

### csv2json

The `csv2json` module converts CSV input into JSON output. Takes STDIN and dumps to STDOUT.

### sqlgen

The `sqlgen` module takes in JSON and dumps SQL lines. Take STDIN and dumps to STDOUT.

## Example Usage

    $ extracter -c <credential file> | csv2json | sqlgen -o <outputfile>

### RA_scraper 

The `master_venues` and `master_promoters` module collects data from ResidentAdvisor and outputs them in Excel file. 

`master_events` uses parts of the collected data and outputs seperate Excel file. 

More info on usage in folder's readme. 
