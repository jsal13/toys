import time


def short_task() -> int:
    """Run a short task."""
    return 0

def long_task() -> int:
    """Run a long task."""
    time.sleep(5)
    return 0

def longer_task() -> int:
    """Run a longer task."""
    time.sleep(5)
    return 0

if __name__ == "__main__":
    pass
