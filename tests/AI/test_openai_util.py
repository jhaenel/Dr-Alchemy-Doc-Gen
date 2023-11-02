import json

import pytest
from unittest.mock import patch, Mock
from src.AI.openai_util import (
    get_api_key,
    create_headers,
    create_body,
    send_request,
    call_openai_api,
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


@patch("http.client.HTTPSConnection")
def test_send_request(mock_http_connection):
    mock_response = Mock()
    mock_response.read.return_value = json.dumps({"result": "success"}).encode("utf-8")
    mock_response.status = 200
    mock_http_connection.return_value.getresponse.return_value = mock_response

    headers = create_headers(TEST_API_KEY)
    body = create_body("Hello!")
    response_data = send_request(headers, body)
    assert json.loads(response_data) == {"result": "success"}


@patch("src.AI.openai_util.send_request")
def test_call_openai_api(mock_send_request, mock_env_vars):
    mock_send_request.return_value = json.dumps({"result": "success"}).encode("utf-8")
    result = call_openai_api("Hello!")
    assert result == {"result": "success"}
