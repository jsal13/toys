-- Used for db_postgres' docker-compose.  See the ``justfile``.

CREATE TABLE events (
    id          serial PRIMARY KEY,
    sensor_id   integer,
    dt          timestamp,
    value_1     integer,
    value_2     float,
    value_3     float,
    heat_index  float,
    power       varchar(6)
);