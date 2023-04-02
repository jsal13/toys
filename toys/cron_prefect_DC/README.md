# Prefect

NOTE: Need to do the docker-compose here, baybee.

## Description

This shows off [Prefect](https://docs.prefect.io/).

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

- Remember to start a work-pool and agent.
  - For example, for work-pool `test` you can start an agent in the following way:

  ```shell
  prefect work-pool create test-pool
  prefect agent start -p 'test-pool'
  ```
