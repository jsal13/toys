# Postgres Docker Compose

## Status

**Working.**

## Description

This is an example of docker-compose running postgres.

## Quickstart

1. If there is no `init.sql` in this directory (or if another table is desired), use `make_example_table.py` to populate the db with a table.
   - Make sure to add this other init script to the docker compose.
2. `docker-compose up`

This will create the sample tables which you can access using the credentials in [the credentials section](#credentials).

## Credentials

**NOTE:** You will need to use `db` in place of `localhost` when calling from the adminer.

- **User**: postgres
- **Password**: example
- **Database**: postgres

## Generating Random Table Data

There is a simple generator, `generate_tables.py`, which generates a `tables.sql` file in `init_scripts/` for the postgres table to insert.
