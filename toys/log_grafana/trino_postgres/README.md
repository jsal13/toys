# Trino + Postgres

## Status

**Working**

## Description

This is an example of docker-compose running postgres with sample tables, as well as a Trino connection to the table.

## Quickstart

**IMPORTANT**: To get the Trino CLI, curl the following: https://repo1.maven.org/maven2/io/trino/trino-cli/385/trino-cli-385-executable.jar.
Remember to `chmod +x` this file before running it.

You may also use a different version of the CLI, though this hasn't been tested here.

1. In terminal, create the containers with 

    ```bash
    docker-compose up
    ```

    > **Note**:
    > If you change anything about postgres tables/data, you will have to remove volumes and stopped containers after running this once due to the way postgres manages its dbs.  
    Use `docker volume prune && docker container prune`.  

2. In another terminal, run:

    ```bash
    ./trino-cli-385-executable.jar --server http://localhost:8080
    ```
    this will bring up the Trino CLI.

3. To test Trino's connection to our postgres db, run a sample command like the following:

    ```sql
    select * from postgres.public.example_long_table limit 10;
    ```

That's it!
