import pytest
import source.service as service
import unittest.mock as mock

@mock.patch("source.service.get_user")
def test_get_user_from_db(mock_get_user):
    mock_get_user.return_value = "mock alice"
    user_name = service.get_user(1)
    assert user_name == "mock alice"