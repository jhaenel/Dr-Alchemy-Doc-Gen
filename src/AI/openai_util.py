import http.client
import json
import os
import logging

from src.util.requests import retry, exception_handler

logging.basicConfig(level=logging.INFO)

API_HOST = "api.openai.com"
API_ENDPOINT = "/v1/chat/completions"
API_MODEL = "gpt-3.5-turbo"
CONTENT_TYPE = "application/json"
ENV_API_KEY = "OPENAI_API_KEY"
SYSTEM_ROLE = "system"
USER_ROLE = "user"
SYSTEM_CONTENT = "You are a staff software engineer."
TIMEOUT = 180


def get_api_key() -> str:
    if api_key := os.environ.get(ENV_API_KEY):
        return api_key
    else:
        raise ValueError(f"The '{ENV_API_KEY}' environment variable is not set.")


def create_headers(api_key: str) -> dict:
    return {"Content-Type": CONTENT_TYPE, "Authorization": f"Bearer {api_key}"}


def create_body(user_content: str) -> str:
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
def send_request(headers: dict, body: str) -> str:
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


@exception_handler
def call_openai_api(content: str) -> dict:
    api_key = get_api_key()
    headers = create_headers(api_key)
    body = create_body(content)
    response_data = send_request(headers, body)
    return json.loads(response_data)

def parse_openai_response(response_data: dict) -> str:
    return response_data["choices"][0]['message']["content"]

def generate(prompt: str) -> str:
    result = call_openai_api(prompt)
    if result is not None:
        return parse_openai_response(result)
    else:
        return None

# Example usage:
if __name__ == "__main__":
    user_content = "Hello!"
    result = call_openai_api(user_content)
    if result is not None:
        print(parse_openai_response(result))
