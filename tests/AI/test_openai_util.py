import pytest

# Constants for testing
TEST_API_KEY = "test-api-key"


@pytest.fixture
def mock_env_vars(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", TEST_API_KEY)

