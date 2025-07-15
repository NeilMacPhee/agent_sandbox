from fastapi.testclient import TestClient
from pydantic_example.main import app
from unittest import mock
from unittest.mock import patch

# set up the test client
client = TestClient(app)

# define the test function
def test_summarize_success():
    # There are three main parts to this test
    # Given
    input_data = {"text": "This is a test input text that is long enough to be summarized."}
    expected_output = input_data["text"][:75] + "..."  # Fake summary logic

    # When
    response = client.post("/summarize", json=input_data)

    # Then
    assert response.status_code == 200
    assert response.json()["summary"] == expected_output

@patch("pydantic_example.main.requests.post")
def test_summarize_external_api_mocked(mock_post):
    # Mock the response object
    mock_response = mock.Mock()
    mock_response.json.return_value = {
        "candidates": [{"output": "Mocked summary output"}]
    }
    mock_response.status_code = 200
    mock_response.raise_for_status = mock.Mock()
    mock_post.return_value = mock_response

    response = client.post("/summarize", json={"text": "This is a test input text."})

    assert response.status_code == 200
    assert response.json()["summary"] == "Mocked summary output"