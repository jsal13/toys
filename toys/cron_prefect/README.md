# Prefect

NOTE: Need to do the docker-compose here, baybee.

## Description

This shows off [Prefect](https://docs.prefect.io/).

## Quickstart

**To run**:

```shell
prefect server start
```

Then create your work-pool and agent as follows:

```shell
prefect work-pool create test-pool
prefect agent start -p 'test-pool'
```

You can put an example flow up using:

```shell
python ./flow_example/deployment.py
```

## Notes

- Remember to start a work-pool and agent.
  - For example, for work-pool `test` you can start an agent in the following way:

  ```shell
  prefect work-pool create test-pool
  prefect agent start -p 'test-pool'
  ```

- You may want to `rm -rf ~/.prefect` to clean up old data or pools.
