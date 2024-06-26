import json
import pytest
from unittest.mock import MagicMock
from put_handler.put_api import lambda_handler, table


def test_put_function_lambda_handler():
    # Mock DynamoDB table update_item response
    table.update_item = MagicMock()

    # Call the lambda_handler function from put-function
    ret = lambda_handler({}, "")

    # Parse the response body as JSON
    response_body = json.loads(ret["body"])

    # Assert the response from the Lambda function
    assert ret["statusCode"] == 200
    assert "message" in response_body
    assert response_body["message"] == "Visitor count updated successfully"
