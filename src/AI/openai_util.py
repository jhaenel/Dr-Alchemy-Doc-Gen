import http.client
import json
import os
import logging

from src.util.requests import retry

# Set up basic logging
logging.basicConfig(level=logging.INFO)

API_HOST = "api.openai.com"
API_ENDPOINT = "/v1/chat/completions"
API_MODEL = "gpt-3.5-turbo"
CONTENT_TYPE = "application/json"
ENV_API_KEY = "OPENAI_API_KEY"
SYSTEM_ROLE = "system"
USER_ROLE = "user"
SYSTEM_CONTENT = "You are a helpful assistant."
TIMEOUT = 180


def get_api_key():
    api_key = os.environ.get(ENV_API_KEY)
    if not api_key:
        raise ValueError(f"The '{ENV_API_KEY}' environment variable is not set.")
    return api_key


def create_headers(api_key):
    return {"Content-Type": CONTENT_TYPE, "Authorization": f"Bearer {api_key}"}


def create_body(user_content):
    return json.dumps(
        {
            "model": API_MODEL,
            "messages": [
                {"role": SYSTEM_ROLE, "content": SYSTEM_CONTENT},
                {"role": USER_ROLE, "content": user_content},
            ],
        }
    )


@retry(exceptions=(http.client.HTTPException,))
def send_request(headers, body):
    connection = http.client.HTTPSConnection(API_HOST, timeout=TIMEOUT)
    try:
        connection.request("POST", API_ENDPOINT, body, headers)
        response = connection.getresponse()
        response_data = response.read()
        if response.status != 200:
            raise http.client.HTTPException(
                f"Request failed: {response.status} {response.reason}"
            )
        return response_data
    finally:
        connection.close()


def call_openai_api(content):
    api_key = get_api_key()
    headers = create_headers(api_key)
    body = create_body(content)
    response_data = send_request(headers, body)
    return json.loads(response_data)


# Example usage:
if __name__ == "__main__":
    user_content = "Hello!"
    try:
        result = call_openai_api(user_content)
        print(result)
    except ValueError as e:
        logging.error(f"Configuration error: {e}")
    except http.client.HTTPException as e:
        logging.error(f"HTTP error occurred after retries: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
