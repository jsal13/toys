# Toys

A collection of toys (templates for how to do things) for Data stuff.

Most of these will be contained to a single folder and do one specific task.  The README in each will tell you the task.

## Prefixes

Nested structures got to be awkward when reusing toys, so I've opted to have a prefix structure on the folder names to say what these toys are or do.  The list of prefixes is given below:

| Prefix | Definition      |
| ------ | --------------- |
| aws    | AWS Service     |
| code   | Code            |
| cron   | Scheduling      |
| db     | Database        |
| k8s    | Kubernetes      |
| mlops  | MLOps           |
| qe     | Query Engine    |
| sec    | Security        |
| stream | Event Streaming |
| tf     | Terraform       |

## Suffixes

As in the prefixes second above, I've opted to use a suffix structure on the folder names to denote how we're building them.  

| Suffix | Definition         |
| ------ | ------------------ |
| DC     | Docker-Compose     |
| K8s    | Kubernetes w/ Helm |

## Why are some toys being copied with a justfile?

There's a lot of different toys that need basic things like a postgres db.  Instead of copy-pasting this each time (making it difficult to update and debug all at once), we use a justfile to copy the toy into a temp folder in the desired toy at runtime.  

For example, if `app_xyz` needs `db_postgres`, we will create an `app_xyz/tmp` folder and copy both `app_xyz` and `db_postgres` into this folder.

This allows us to have toys which utilize other toys, but which we can gitignore easily.  

## OLD STUFF HERE

### Toys that need Work

- `aws/sns_eventbridge`
- `logging_and_monitoring/grafana`
  - Get Trino working.
  - Isolate original api.py (as there is another API as well now).

### Other TODO

- TO CHECK:
  - query_engine

### Making a New Toy

The only requirements are:

- [ ] The folder must contain a README made from `README.md.tmpl`.
- [ ] The folder must have one of the following (if applicable):
  - Dockerfiles or a docker-compose.yaml
  - Terraform-related files
  - Helm-related files
- [ ] Python Folders should use `ssh://git@github.com/jsal13/cookiecutter-pytemplate`.
