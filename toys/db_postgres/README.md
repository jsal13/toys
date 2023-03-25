# Postgres Docker Compose

## Description

This is an example of docker-compose running postgres.

## Prereqs

If there is no `init.sql` in this directory (or if another table is desired), use `make_example_table.py` to populate the db with a table.

- Make sure to add this other init script to `docker-compose.yaml`.

## Quickstart

To run:

```shell
just run
```

To clean up:

```shell
just clean
```

This will create the sample tables which you can access using the credentials in [the credentials section](#credentials) via adminer at <http://localhost:8080>.

## Credentials

**NOTE:** You will need to use `db` in place of `localhost` when calling from the adminer.

|          |            |
| -------- | ---------- |
| User     | `postgres` |
| Password | `example`  |
| Database | `postgres` |
