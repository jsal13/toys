-- Used for db_postgres' docker-compose.  See the ``justfile``.

CREATE TABLE kafka_example (
    id          serial PRIMARY KEY,
    dt          timestamp,
    value1      integer,
    value2      float,
    power       varchar(6)
);
