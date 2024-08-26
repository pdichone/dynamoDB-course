import boto3
from boto3.dynamodb.conditions import Key


def query_books_by_isbn_price(isbn, min_price, max_price, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("Books")
    response = table.query(
        IndexName="PriceIndex",
        KeyConditionExpression=Key("ISBN").eq(isbn)
        & Key("Price").between(min_price, max_price),
        ProjectionExpression="ISBN, Title, Price, #yr, Info.subtitle, Info.authors, Info.short_description, Info.page_count, Info.categories",
        ExpressionAttributeNames={"#yr": "Year"},
    )
    return response["Items"]


if __name__ == "__main__":
    books_in_price_range = query_books_by_isbn_price(
        "28e13564-1fbb-4dbf-9add-25a5e020d14e", 10, 50
    )
    for book in books_in_price_range:
        print(book)
