# Grafana

## Status

**Working.**
**MUST ADD TRINO.**

## Description

This project creates an instance of Grafana and Prometheus.  It also sets up:

- An API up in Python in `api.py` for Prometheus to ping every few seconds,
- A postgres DB with a timeseries metric table for Grafana can connect to,

```mermaid
graph TD
    A(Grafana):::grafana
    B(Prometheus):::prometheus
    C(PYTHON_API):::python_api
    D(DB):::postgres

    classDef prometheus fill:#660033;
    classDef grafana fill:#006633;
    classDef python_api fill:#994400;
    classDef postgres fill:#003366;


    B.-|Pings the <br/>/metrics endpoint|C
    A---|Connects to|B
    A---|Connects to|D
```

## Quickstart

```bash
docker-compose up
```

Then you can go to:
    - <http://localhost:9090> for Prometheus
    - <http://localhost:3000> for Grafana

See [the credentials](#credentials) section below for login information.  Feel free to "Skip" the section which tries to make you set a new password in Grafana.

## Credentials

> **Note**
> You will need to use `db` in place of `localhost` when calling postgres from the adminer.

- **Postgres User**: `postgres`
- **Postgres Password**: `example`
- **Postgres Database**: `postgres`
- **Grafana Username**: `admin`
- **Grafana Password**: `admin`

## Exporting Query Results from Prometheus

At times, we may want to query results from Prometheus and save them elsewhere, like to a CSV for import into some other DB.  We can do this as follows:

```bash
curl -g 'http://localhost:9090/api/v1/query?query=http_requests_total{job="api",handler="/metrics",method="GET"}[1m]'
```

Notice here that we are using `-g` which takes out the "glob" rules, allowing us to use brackets and parens in the URL.  The rest is hitting the endpoint with the appropriate query.  The results look like this (expanded out for easier reading):

```json
{
  "status":"success",
  "data":
    {
      "resultType":"matrix",
      "result":
        [
          {
            "metric":
              {
                "__name__":"http_requests_total",
                "handler":"/metrics",
                "instance":"api:8000",
                "job":"api",
                "method":"GET",
                "status":"2xx"
              },
            "values":
              [
                [1663190851.991,"186"],
                [1663190861.991,"187"],
                [1663190871.990,"188"],
                [1663190881.990,"189"],
                [1663190891.990,"190"],
                [1663190901.990,"191"]
              ]
          }
        ]
    }
}
```

Notice the `data > result > values` gives us a list of timestamps and associated values.  These can be taken into Python and exported to a CSV, or whatever else you'd like to do with it.
