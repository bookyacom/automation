'use strict';

import db from '../connection';

const TABLE_NAME = 'Award';
const AWARDED_TABLE_NAME = 'Awarded';

export const updateAwarded = function *({awards}, profileID) {
	const keys = Object.keys(awards);
	if (keys.length === 0) {
		return;
	}

	for (let key of keys) {
		let award = key;
		let awarded = awards[key];
		award = award.replace(/_/g, ' ');
		award = yield db
			.select()
			.from(TABLE_NAME)
			.where(`title.toLowerCase() = "${award}"`)
			.one();

		if (award) {
			for (let year of Object.keys(awarded)) {
				const value = awarded[year];
				if (value.trim()) {
					yield db
						.create('edge', AWARDED_TABLE_NAME)
						.set({
							title: year,
							value
						})
						.from(profileID)
						.to(award['@rid'])
						.one()
						.catch(e => {
							console.error(e);
							return null;
						});
				}
			}
		}
	}
}
