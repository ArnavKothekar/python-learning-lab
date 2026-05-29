import pytest
import source.service as service
import unittest.mock as mock

@mock.patch("source.service.get_user")
def test_get_user_from_db(mock_get_user):
    mock_get_user.return_value = "mock alice"
    user_name = service.get_user(1)
    assert user_name == "mock alice"

@mock.patch("requests.get")
def test_get_user_api(mock_requests_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"id": 1, "name": "john doe"}]
    mock_requests_get.return_value = mock_response

    users = service.get_user_api()
    assert users[0]["name"] == "john doe"