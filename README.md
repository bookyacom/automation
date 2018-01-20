# Scrapers Microservice [![CircleCI](https://circleci.com/gh/bookyacom/automation.svg?style=shield&circle-token=66909009a6cbe9867570d6a0b57ac9a3a478cf2e)](https://circleci.com/gh/bookyacom/automation) [![Dependency Status](https://gemnasium.com/badges/46e9471bd3124a106fcccc72daa51302.svg)](https://gemnasium.com/github.com/bookyacom/automation) [![codecov](https://codecov.io/gh/bookyacom/automation/branch/master/graph/badge.svg?token=OP0xgyFxWU)](https://codecov.io/gh/bookyacom/automation)

> This is Bookya Scrapers microservice repository that use Python framework.

## Requirements
- [Python 2.7](https://www.python.org) at least

## Get started
>TODO: https://gist.github.com/PurpleBooth/109311bb0361f32d87a2

If you want to learn more about ``setup.py`` files, check out [Setup](https://github.com/kennethreitz/setup.py).

### RA_scraper

The `master_venues` and `master_promoters` module collects data from ResidentAdvisor and outputs them in Excel file.

`master_events` uses parts of the collected data and outputs seperate Excel file.

More info on usage in folder's readme.

### Partyflock scraper
This scraper will collect all the information (biography, socials, labels etc.) of DJs on Partyflock that had an event in 2017, 2018 and are not already listed in the Bookya database.

More info on usage in folder's readme.

## Tests
>TODO

## Contributing
If you are new to this repository, please read [development doc](/docs/development.md) first. We have project documentation under [docs/documentation](/docs/documentation).

## License
Bookya Sdn Bhd.
