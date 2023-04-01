import string

from toys.cron_prefect_DC.flow_example.example_names import NAMES
from prefect import flow, task
from prefect.task_runners import ConcurrentTaskRunner, SequentialTaskRunner


@task(retries=2, timeout_seconds=500)
def name_to_score(name: str) -> int:
    """Convert ``name`` into a score based on the letters."""
    return sum(string.ascii_lowercase.index(letter) for letter in name)


@task(retries=2, timeout_seconds=500)
def clean_name(name: str) -> str:
    """Clean the name for use in other functions."""
    return "".join(letter for letter in name.lower() if letter.isalpha())


@flow(
    name="Score Name",
    description="Scores a name",
    version="1",
    retries=2,
    timeout_seconds=500,
    task_runner=SequentialTaskRunner,
)
def score_name(name: str) -> int:
    """Score a name."""
    name_cleaned = clean_name(name=name)
    return name_to_score(name=name_cleaned)


@flow(
    name="Score a Few Names",
    description="Scores a few names",
    version="1",
    retries=2,
    timeout_seconds=500,
    task_runner=ConcurrentTaskRunner,
)
def score_a_few_names(names: list[str]) -> int:
    """Score a name."""
    for name in names:
        name_cleaned = clean_name.submit(name=name)
        score = name_to_score.submit(name=name_cleaned)
        print(score)


if __name__ == "__main__":
    score_a_few_names(names=NAMES)
