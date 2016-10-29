#!/bin/bash


echo "Manually removing database with LUCENE INDEX located at $DB_PWD"
sh -c "orientdb stop"
sleep 2
sh -c "rm -rf $DB_PWD"
sh -c "orientdb start"
