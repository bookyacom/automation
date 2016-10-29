#!/bin/bash

echo $1
export PGPASSWORD=$PSQL_PASSWORD
DB_NAME=$PSQL_DB
: ${DB_NAME:="test"}
: ${PSQL_HOST:="localhost"}
: ${PSQL_PORT:=5432}
echo $DB_NAME

check_database() {
  echo "-- execute check database"
  sh -c "psql template1 -h $PSQL_HOST -p $PSQL_PORT -U $PSQL_USERNAME -d $1 -c \"SELECT 1 AS result FROM pg_database WHERE datname='$1'\"" >/dev/null 2>&1
}

create_database() {
  echo "-- execute create database"
  sh -c "psql -h $PSQL_HOST -p $PSQL_PORT -U $PSQL_USERNAME -d template1 -c \"create database $1\""
}

run_query() {
  echo "-- execute queries"
  sh -c "psql -h $PSQL_HOST -p $PSQL_PORT -U $PSQL_USERNAME -d $DB_NAME -a -f $PWD/script/postgresql.schema.sql"
}

drop_database() {
  echo "-- droping database"
  sh -c "psql template1 -h $PSQL_HOST -p $PSQL_PORT -U $PSQL_USERNAME -c \"drop database $1\""
}

if [ "$1" = "create" ]
then
  if ! check_database $DB_NAME; then
    echo "-- database do not exists"
    create_database "$DB_NAME"
  fi
  run_query
  echo "-- done --"
  exit 0
fi

if [ "$1" = "drop" ]
then
  if check_database $DB_NAME; then
    echo "-- database exists"
    drop_database "$DB_NAME"
  fi
  echo "-- done --"
  exit 0
fi
