#!/bin/bash

psql -U postgres -d dota2 -c "DELETE FROM hero;"
psql -U postgres -d dota2 -c "DELETE FROM player;"
psql -U postgres -d dota2 -c "COPY hero(hero_id, hero_name, pro_Win, pro_pick)
FROM '/usr/src/heroes.csv' DELIMITER ',' CSV HEADER;"

psql -U postgres -d dota2 -c "COPY player(player_id, rank_tier, win, lose, mmr_estimate)
FROM '/usr/src/players.csv' DELIMITER ',' CSV HEADER;"
