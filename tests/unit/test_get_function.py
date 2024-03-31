import json
import pytest
from unittest.mock import MagicMock
from get_handler.get_api import lambda_handler, table

@pytest.fixture()
def apigw_event():
    """ Generates API GW Event for get-function"""
    # Define event data for get-function
    event = {
        # Define event data here...
    }
    return event

def test_get_function_lambda_handler(apigw_event):
    # Mock DynamoDB table query response
    table.query = MagicMock(return_value={'Items': [{'visitors': 10}]})

    # Call the lambda_handler function from get-function
    ret = lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    # Assert the response from the Lambda function
    assert ret["statusCode"] == 200
    assert "count" in ret["body"]
    assert data["count"] == 10  # Change 10 to the expected count value
