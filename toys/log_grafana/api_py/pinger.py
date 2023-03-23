import time
import random

import requests

ENDPOINT = "http://api_py:8000/"


def make_random_requests_quickly(num_pings: int) -> None:
    """Make ``num_pings`` random requests in a burst."""
    for _ in range(num_pings):
        requests.get(ENDPOINT, timeout=300)
        time.sleep(0.1)


while True:
    # Ping the server ``n`` tines in burst.
    num = random.randint(1, 10)
    make_random_requests_quickly(num)

    # Wait for a random amount of time.
    sleep_secs = random.randint(1, 15)
    time.sleep(sleep_secs)
