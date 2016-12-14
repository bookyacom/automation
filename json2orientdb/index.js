'use strict';

require('babel/register');

module.exports = (type) => {
	switch (type) {
		case 'promoter':
			require('./json2orientdb');
			break;
		case 'venue':
			require('./venue');
			break;
		default:
	}
}
