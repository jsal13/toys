# Postgres

Read the docs for this chart [here](https://artifacthub.io/packages/helm/bitnami/postgresql).

## Quick Start

Have a K8s cluster running (we use `kind` here):

```shell
kind create cluster
```

Install the chart with custom `values.yaml`:

```shell
helm install postgres -f ./values.yaml bitnami/postgresql
```

Port forward with:

TODO: try this without the &?

```shell
kubectl port-forward --namespace default svc/postgres-postgresql 5432:5432 &
```

### Cleaning Up

1. Kill the port-forwarding process.  You may have to kill this process in `ps -aux | grep port-forward`.
2. Uninstall the chart:

```shell
helm uninstall postgres
```

If you're done with the cluster:

```shell
kind delete cluster
```

## Credentials

| user     | password | database |
| -------- | -------- | -------- |
| postgres | example  | postgres |
