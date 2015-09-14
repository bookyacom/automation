# automation
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