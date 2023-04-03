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

**To clean up**:

```shell
just clean
```

## Notes

- We mount several things into the Trino image.  These are described [here](https://github.com/trinodb/trino/blob/master/core/docker/README.md).
