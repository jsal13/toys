from datetime import datetime, timedelta
from dataclasses import dataclass
import os
import random

# import psycopg2


@dataclass
class Metric:
    """Metric object for a row in a Long Format table."""

    name: str
    value: float
    date_time: str


class ExampleTableLongFormat:
    def __init__(self, table_name: str, table_creation_cols, num_metrics: int = 2):
        """
        Return queries corresponding to a table type.

        Return creation/insert queries corresponding to a long-format example
        table with ``num_metrics`` different "name of metric" values.
        """
        self.table_name = table_name
        self.table_creation_cols = table_creation_cols
        self.num_metrics = num_metrics

    def create_table(self) -> str:
        """Drop and Create the table."""
        return f"""
        DROP TABLE IF EXISTS {self.table_name};
        CREATE TABLE IF NOT EXISTS {self.table_name} ({self.table_creation_cols});

        """

    def _generate_random_metric(self, dt: str) -> Metric:
        metric_name = f"metric_{random.randint(1, self.num_metrics)}"
        metric_value = random.random()
        return Metric(metric_name, metric_value, dt)

    def _insert_row(self, dt: str):
        metric = self._generate_random_metric(dt)
        return f"""('{metric.date_time}', '{metric.name}', {metric.value})"""

    def insert_n_rows(self, n: int, randomize_time_between: bool = True):
        """Insert ``n`` rows into the table at randomized or steady time intervals."""
        query = f"INSERT INTO {self.table_name} (dt,name,value) VALUES \n"
        rows = []
        original_dt = datetime.now()
        for _ in range(n):
            if randomize_time_between:
                current_dt_iso = (
                    original_dt + timedelta(seconds=2 * random.random())
                ).isoformat()
            else:
                current_dt_iso = (original_dt + timedelta(seconds=1)).isoformat()
            rows.append(self._insert_row(current_dt_iso))
        return query + ",\n".join(rows) + ";\n"


def run_query_with_connection(conn, query: str):
    """Run ``query`` with a db connection ``conn``."""
    with conn.cursor() as cur:
        cur.execute(query)
        conn.commit()
    print("* Query complete.")


def write_query_to_file(output_loc: str, query: str):
    """Write ``query`` to a file at ``output_loc``."""
    with open(output_loc, "w+", encoding="utf-8") as f:
        f.write(query)


if __name__ == "__main__":
    HOST = "localhost"
    DATABASE = "postgres"
    USER = "postgres"
    PASSWORD = "example"

    NUM_INITIAL_ROWS = 100

    EXAMPLE_TABLE_LONG_FORMAT_TABLE_NAME = "example_long_table"
    EXAMPLE_TABLE_LONG_FORMAT_CREATION_COLUMNS = """
    dt TIMESTAMP NOT NULL,
    name VARCHAR NOT NULL,
    value FLOAT
    """

    REPO_ROOT = os.path.expanduser("~/repos/de_toys/")
    OUTPUT_PATH = os.path.join(REPO_ROOT, "_assets", "init_scripts/init.sql")


    # Create example table.
    etlf = ExampleTableLongFormat(
        table_name=EXAMPLE_TABLE_LONG_FORMAT_TABLE_NAME,
        table_creation_cols=EXAMPLE_TABLE_LONG_FORMAT_CREATION_COLUMNS,
        num_metrics=2,
    )
    QUERY = etlf.create_table()
    QUERY += etlf.insert_n_rows(NUM_INITIAL_ROWS)

    write_query_to_file(output_loc=OUTPUT_PATH, query=QUERY)
