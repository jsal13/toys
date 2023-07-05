import os

import pyarrow as pa
import pyarrow.parquet as pq
from sklearn.datasets import make_classification


def generate_parquet(
    ncols: int = 5,
    nrows: int = 1000,
    nfiles: int = 1,
    where: str = "./toys/code_python/pq_pyarrow/data",
) -> None:
    """
    Generate ``nfiles`` parquet files with ``nrows`` rows and ``ncols`` cols.

    Parameters
    ----------
    ncols : int, optional
        Number of columns, by default 5
    nrows : int, optional
        Number of rows, by default 1000
    nfiles : int, optional
        Number of parquet files, by default 1
    where : str, optional
        Path to the files, by default "."

    """
    for idx in range(nfiles):
        data, _ = make_classification(n_samples=nrows, n_features=ncols)
        data_with_cols = {
            f"f_{col_num}": data[:, col_num] for col_num in range(data.shape[1])
        }
        pq_table = pa.table(data_with_cols)
        pq.write_table(
            table=pq_table, where=os.path.join(where, f"pq_file_{idx:02}.parquet")
        )


if __name__ == "__main__":
    generate_parquet(nrows=1000000, ncols=20, nfiles=5)
