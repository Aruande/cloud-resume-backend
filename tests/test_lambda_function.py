import json
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

# Tell Python where to find our Lambda function
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))


def test_lambda_returns_updated_visitor_count():
    # Simulate DynamoDB
    mock_dynamodb = MagicMock()
    mock_table = mock_dynamodb.Table.return_value

    # Pretend DynamoDB updated the visitor count to 42
    mock_table.update_item.return_value = {
        "Attributes": {"count": 42}
    }

    # Replace the real AWS connection with our mock
    with patch("boto3.resource", return_value=mock_dynamodb):
        sys.modules.pop("lambda_function", None)
        import lambda_function

        response = lambda_function.lambda_handler({}, None)

    # Verify the Lambda response
    assert response["statusCode"] == 200
    assert json.loads(response["body"]) == {"count": 42}

    # Verify DynamoDB was called exactly once
    mock_table.update_item.assert_called_once()