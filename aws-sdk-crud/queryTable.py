import boto3
from boto3.dynamodb.conditions import Key, Attr

# === must pip install boto3 ===


def query_books(isbn, title=None, year=None, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")
        # Explicitly specify a region
        # dynamodb = boto3.resource('dynamodb',region_name='us-west-2')

    table = dynamodb.Table("Books")

    if title:
        response = table.query(
            KeyConditionExpression=Key("ISBN").eq(isbn) & Key("Year").eq(year)
        )
    else:
        response = table.query(KeyConditionExpression=Key("ISBN").eq(isbn))

    return response["Items"]


if __name__ == "__main__":
    query_isbn = "a6bb6788-7183-46b6-9eed-610517417bc6"  # Example ISBN, replace with actual ISBN to query
    query_title = "Sample Book Title 40"  # Optional: replace with actual title to narrow the search
    year = 2020
    print(f"Books with ISBN {query_isbn}")
    books = query_books(query_isbn, query_title, year=year)
    for book in books:
        print(book)
