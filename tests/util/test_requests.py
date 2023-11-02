from unittest.mock import Mock
from src.util.requests import retry, MAX_RETRIES

import pytest


# Function to be decorated for testing purposes
def always_fail():
    raise ValueError("Simulated Failure")


def succeeds_on_nth_try(n):
    call_count = [0]  # Using a list to have a mutable integer

    def _inner():
        if call_count[0] < n - 1:
            call_count[0] += 1
            raise ValueError("Simulated Failure")
        return "Success"

    return _inner, call_count


def test_retry_decorator(mocker):
    mocker.patch("time.sleep")
    test_func, call_count = succeeds_on_nth_try(3)

    # Apply the retry decorator
    decorated_func = retry(
        exceptions=(ValueError,), tries=MAX_RETRIES, delay=1, backoff=2
    )(test_func)

    result = decorated_func()

    assert result == "Success"

    assert call_count[0] == 2  # Function should succeed on the 3rd try


def test_retry_decorator_exceeds_max_retries(mocker):
    mock_sleep = mocker.patch("time.sleep")
    test_func = always_fail

    # Apply the retry decorator
    decorated_func = retry(
        exceptions=(ValueError,), tries=MAX_RETRIES, delay=1, backoff=2
    )(test_func)

    with pytest.raises(ValueError) as exc_info:
        decorated_func()

    # The exception message should be the one raised by the always_fail function
    assert "Simulated Failure" in str(exc_info.value)

    # Verify the function was called MAX_RETRIES times
    # Here we can actually use a Mock to wrap the always_fail function to count calls
    test_func_mock = Mock(side_effect=always_fail)
    decorated_func = retry(
        exceptions=(ValueError,), tries=MAX_RETRIES, delay=1, backoff=2
    )(test_func_mock)

    with pytest.raises(ValueError):
        decorated_func()

    assert test_func_mock.call_count == MAX_RETRIES
