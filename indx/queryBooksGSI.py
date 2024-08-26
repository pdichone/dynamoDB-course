import boto3
from boto3.dynamodb.conditions import Key


def query_books_by_author(author, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("Books")

    # Describe the table to check the status of the GSI
    client = boto3.client("dynamodb")
    table_description = client.describe_table(TableName="Books")
    # print("Table description:", table_description)

    # Check if the Author attribute exists in any item
    # scan_response = table.scan(ProjectionExpression="Author")
    # authors = {item.get("Author", None) for item in scan_response["Items"]}
    # print("Authors in the table:", authors)

    response = table.query(
        IndexName="AuthorPriceIndex",
        KeyConditionExpression=Key("Author").eq(author),
        ProjectionExpression="ISBN, Title, Author, Price, #yr, Info.subtitle, Info.authors, Info.short_description, Info.page_count, Info.categories",
        ExpressionAttributeNames={"#yr": "Year"},
    )
    return response["Items"]


if __name__ == "__main__":
    # books_by_author = query_books_by_author("Hannu Rajaniemi")
    books_by_author = query_books_by_author("Author 34")
    for book in books_by_author:
        print(book)
