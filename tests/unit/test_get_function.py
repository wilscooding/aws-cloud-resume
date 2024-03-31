from unittest.mock import MagicMock
import pytest
from get_api import get_count


# Mocking DynamoDB table
@pytest.fixture
def dynamodb_table_mock():
    table_mock = MagicMock()
    table_mock.query.return_value = {
        'Items': [{'visitors': 10}]}  # Mock response from DynamoDB
    return table_mock


def test_get_count_with_mock(dynamodb_table_mock):
    count = get_count(dynamodb_table_mock)
    assert count == 10  # Assert that the count matches the expected value
