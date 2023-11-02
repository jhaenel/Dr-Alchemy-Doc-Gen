import time
import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)

MAX_RETRIES = 5
RETRY_BACKOFF_START = 1


def retry(exceptions, tries=MAX_RETRIES, delay=RETRY_BACKOFF_START, backoff=2):
    """
    Retry decorator with exponential backoff.

    Parameters:
        exceptions: A tuple of exception classes; on these exceptions, the function will retry.
        tries: Total number of tries.
        delay: Initial delay between retries in seconds.
        backoff: Backoff multiplier (e.g., value of 2 will double the delay each retry).
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            mdelay = delay
            for attempt in range(tries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == tries - 1:
                        raise
                    logging.warning(f"Retrying in {mdelay} seconds...")
                    time.sleep(mdelay)
                    mdelay *= backoff

        return wrapper

    return decorator
