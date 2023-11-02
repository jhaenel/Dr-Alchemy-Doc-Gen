import http.client
import json
import os

API_HOST = "api.openai.com"
API_ENDPOINT = "/v1/chat/completions"
API_MODEL = "gpt-3.5-turbo"
CONTENT_TYPE = "application/json"
ENV_API_KEY = "OPENAI_API_KEY"
SYSTEM_ROLE = "system"
USER_ROLE = "user"
SYSTEM_CONTENT = "You are a helpful assistant."


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


def send_request(headers, body):
    connection = http.client.HTTPSConnection(API_HOST)
    connection.request("POST", API_ENDPOINT, body, headers)
    response = connection.getresponse()
    response_data = response.read()
    connection.close()

    if response.status != 200:
        raise Exception(f"Request failed: {response.status} {response.reason}")
    return response_data


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
    except Exception as e:
        print(f"An error occurred: {e}")
