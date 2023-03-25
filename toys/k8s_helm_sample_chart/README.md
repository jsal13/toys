# SampleChart

## Description

Basic example of using Helm to create an application on K8s.  Follows [this tutorial](https://helm.sh/docs/chart_template_guide/getting_started/).

Directory created with `helm create (project-name)`.

## Quickstart

1. Start up a k3d cluster:

    ```shell
    k3d cluster create cool-salamander
    ```

2. Install the chart:

    ```shell
    helm install cool-salamander .
    ```

## Validating and Linting

Make sure k3d is running.

```shell
# Linting.
heml lint .

# Templating dry-run.
helm install cool-salamander . --debug --dry-run
```
