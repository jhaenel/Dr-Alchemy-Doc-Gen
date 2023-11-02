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

