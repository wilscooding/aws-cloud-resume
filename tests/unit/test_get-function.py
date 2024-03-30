# test_get_function.py

import json
import pytest

from get_function import lambda_handler


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event for get-function"""
    # Define event data for get-function
    event = {
        # Define event data here...
    }
    return event


def test_get_function_lambda_handler(apigw_event):
    # Call the lambda_handler function from get-function
    ret = lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    # Assert the response from the Lambda function
    assert ret["statusCode"] == 200
    assert "count" in ret["body"]
    # Add more assertions based on the expected behavior of your function
