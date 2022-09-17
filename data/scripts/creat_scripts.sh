#!/bin/bash
psql -U postgres -c "\set AUTOCOMMIT on"
# create dota2 database if not exists.
psql -U postgres -tc "SELECT 1 FROM pg_database WHERE datname = 'dota2'" | grep -q 1 | psql -U postgres -c "CREATE DATABASE dota2"
# psql -U postgres -c "CREATE DATABASE dota2;"

# connect to dota2 database and create tables.
psql -U postgres -d dota2 -c "
CREATE TABLE IF NOT EXISTS hero (
  hero_id INTEGER NOT NULL, 
  hero_name character varying,
  pro_Win INTEGER,
  pro_pick INTEGER
);
CREATE TABLE IF NOT EXISTS player (
  player_id REAL NOT NULL, 
  rank_tier REAL,
  win REAL,
  lose REAL,
  mmr_estimate REAL
);"