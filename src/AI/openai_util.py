import os

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

