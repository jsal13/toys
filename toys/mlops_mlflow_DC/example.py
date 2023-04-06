import argparse
import random

import mlflow
import numpy as np


def example_experiment_run() -> None:
    """Run example MLFlow experiment."""
    experiment = mlflow.set_experiment("test")
    print("> mlflow tracking uri:", mlflow.tracking.get_tracking_uri())

    with mlflow.start_run(experiment_id=experiment.experiment_id):
        butts = random.randint(0, 10)
        cool = random.random()
        norm = np.random.normal()

        mlflow.log_metrics({"butts": butts, "cool": cool, "norm": norm})


if __name__ == "__main__":
    # Number of runs, parses command line stuff.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        type=int,
        default=10,
        nargs="?",
        help="Number of runs of an experiment (default: 10)",
    )
    num_runs = vars(parser.parse_args())["n"]

    # MLFlow Portion
    mlflow.set_tracking_uri("http://0.0.0.0:5000")

    for iter_num in range(1, num_runs + 1):
        print(f"> Running example.py (Iteration {iter_num})")
        example_experiment_run()
