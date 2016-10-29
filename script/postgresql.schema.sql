-- Enable PostGIS (includes raster)
CREATE EXTENSION postgis;
-- Enable Topology
CREATE EXTENSION postgis_topology;

CREATE TYPE action_type as enum('ANSWER_QUESTION', 'SKIP_QUESTION', 'SKIP_ALL_QUESTIONS', 'SELECT_GENRE',
                        'UNSELECT_GENRE', 'MORE_GENRE', 'CHANGE_FROM_DATE', 'CHANGE_TO_DATE',
                        'CHANGE_LOCATION',  'CHANGE_FILTER', 'VIEW_PROFILE', 'PLAY_FEATURED_TRACK',
                        'FOLLOW_PROFILE', 'UNFOLLOW_PROFILE', 'REJECT_PROFILE', 'MESSAGE_PROFILE',
                        'VIEW_NOTIFICATION');

CREATE TABLE IF NOT EXISTS activities (
  id serial PRIMARY KEY,
  action action_type,
  created_on timestamp,
  value text,
  created_at timestamp with time zone NOT NULL,
  updated_at timestamp with time zone NOT NULL,
  did varchar(100),
  uid varchar(100)
);


CREATE TYPE location_type as enum('country', 'poi', 'provience', 'district', 'region', 'city', 'state');

CREATE TABLE if not exists locations
(
  id serial NOT NULL,
  name character varying(255) NOT NULL,
  unit character varying(255),
  street character varying(255),
  full_address text,
  region character varying(255),
  state character varying(255),
  postcode character varying(255),
  district character varying(255),
  city character varying(255),
  provience character varying(255),
  country character varying(255),
  point geography(POINT) not null,
  pg_zone geography(POLYGON),
  type location_type,
  created_at timestamp with time zone NOT NULL,
  updated_at timestamp with time zone NOT NULL,
  CONSTRAINT locations_pkey PRIMARY KEY (id)
);
