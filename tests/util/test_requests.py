from src.util.requests import retry, MAX_RETRIES

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
    mock_sleep = mocker.patch("time.sleep")
    test_func, call_count = succeeds_on_nth_try(3)

    # Apply the retry decorator
    decorated_func = retry(
        exceptions=(ValueError,), tries=MAX_RETRIES, delay=1, backoff=2
    )(test_func)

    result = decorated_func()

    assert result == "Success"

    assert call_count[0] == 2  # Function should succeed on the 3rd try


