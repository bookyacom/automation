'use strict';

const meow = require('meow');
const jsonorientdb = require('./json2orientdb');

const cli = meow(`
	Usage
		$ bookya-automation

	Options
		-t, --type type of automation ingestion

	Examples
		$ cat agencies.json | bookya-automation --type="agency"
`, {
	alias: {
		t: 'type'
	},
	default: {
		type: 'artist'
	}
});

switch (cli.flags.type) {
	case 'artist':
		jsonorientdb(cli.flags.type);
		break;
	case 'venue':
		jsonorientdb(cli.flags.type);
		break;
	default:
		console.error(new Error('Not supporting this type'));
		process.exit(1);
}
