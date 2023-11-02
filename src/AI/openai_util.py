import os

ENV_API_KEY = "OPENAI_API_KEY"


def get_api_key():
    api_key = os.environ.get(ENV_API_KEY)
    if not api_key:
        raise ValueError(f"The '{ENV_API_KEY}' environment variable is not set.")
    return api_key

