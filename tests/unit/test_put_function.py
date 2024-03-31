import json
import pytest

from put-function.put-function import lambda_handler


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event for put-function"""
    # Define event data for put-function
    event = {
        # Define event data here...
    }
    return event


def test_put_function_lambda_handler(apigw_event):
    # Call the lambda_handler function from put-function
    ret = lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    # Assert the response from the Lambda function
    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    # Add more assertions based on the expected behavior of your function
