import boto3

def create_books_table_with_gsi(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName='Books',
        KeySchema=[
            {
                'AttributeName': 'ISBN',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'Year',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'ISBN',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'Year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'Author',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'Price',
                'AttributeType': 'N'
            }
        ],
        GlobalSecondaryIndexes=[
            {
                'IndexName': 'AuthorPriceIndex',
                'KeySchema': [
                    {
                        'AttributeName': 'Author',
                        'KeyType': 'HASH'  # Partition key
                    },
                    {
                        'AttributeName': 'Price',
                        'KeyType': 'RANGE'  # Sort key
                    }
                ],
                'Projection': {
                    'ProjectionType': 'ALL'  # Include all attributes
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10
                }
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table

if __name__ == '__main__':
    books_table = create_books_table_with_gsi()
    print("Table status:", books_table.table_status)
