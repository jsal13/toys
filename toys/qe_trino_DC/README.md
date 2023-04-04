# Trino with Docker Compose

## Description

[Trino](https://trino.io/) is a query engine.  We can query databases (like postgres) and a [variety of other things](https://trino.io/docs/current/connector.html).

We demonstrate Trino with the following connectors:

- Postgres

## Quickstart

**To run**:

```shell
just run
```

To query the database, download the [Trino CLI](https://trino.io/docs/current/client/cli.html) and use the command:

```shell
./trino-cli.jar --server http://localhost:8081 --catalog postgres --schema public
```

From inside the CLI you can query a table:

```sql
SELECT * FROM sensors;
```

**To clean up**:

```shell
just clean
```

## Notes

- We mount several things into the Trino image.  These are described [here](https://github.com/trinodb/trino/blob/master/core/docker/README.md).
