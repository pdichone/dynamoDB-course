import boto3


# === must pip install boto3 ===
def create_books_table(dynamodb=None):
    if not dynamodb:
        # dynamodb = boto3.resource('dynamodb')
        # dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
        dynamodb = boto3.resource("dynamodb", region_name="us-west-2")

    table = dynamodb.create_table(
        TableName="Books",
        KeySchema=[
            {"AttributeName": "ISBN", "KeyType": "HASH"},  # Partition key
            {"AttributeName": "Year", "KeyType": "RANGE"},  # Sort key
        ],
        AttributeDefinitions=[
            {"AttributeName": "ISBN", "AttributeType": "S"},
            {"AttributeName": "Year", "AttributeType": "N"},
            # {"AttributeName": "Title", "AttributeType": "S"},
        ],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
    )
    return table


if __name__ == "__main__":
    books_table = create_books_table()
    print("Table Name:", books_table.table_name)
    print("Table status:", books_table.table_status)
    print("Table ARN:", books_table.table_arn)  # Amazon Resource Name
    client = boto3.client("dynamodb")
    response = client.describe_table(TableName="Books")
    print("Table desc:", response)
