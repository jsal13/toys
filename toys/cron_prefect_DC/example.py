import time

from prefect import flow


@flow
def short_task() -> int:
    """Run a short task."""
    return 2


@flow
def long_task() -> int:
    """Run a long task."""
    time.sleep(5)
    return 3


@flow
def longer_task() -> int:
    """Run a longer task."""
    time.sleep(5)
    return 5


@flow
def longer_and_long_task() -> int:
    """Run both longer and long task."""
    return longer_task() * long_task()


if __name__ == "__main__":
    print(short_task())
    print(long_task())
    print(longer_task())
    print(longer_and_long_task())
