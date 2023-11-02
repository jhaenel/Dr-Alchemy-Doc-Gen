import pytest
from src.AI.openai_util import (
    get_api_key,
    create_headers,
    create_body,
)

# Constants for testing
TEST_API_KEY = "test-api-key"


@pytest.fixture
def mock_env_vars(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", TEST_API_KEY)


def test_get_api_key(mock_env_vars):
    assert get_api_key() == TEST_API_KEY


def test_create_headers():
    expected_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TEST_API_KEY}",
    }
    headers = create_headers(TEST_API_KEY)
    assert headers == expected_headers


def test_create_body():
    user_content = "Hello!"
    body = create_body(user_content)
    assert "gpt-3.5-turbo" in body
    assert "messages" in body

