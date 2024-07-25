from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Attr


def scan_books(year_range, display_books, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("Books")
    scan_kwargs = {
        "FilterExpression": Attr("Year").between(*year_range),
        "ProjectionExpression": "ISBN, Title, Info.subtitle, Info.authors, Info.short_description, Info.page_count, Info.categories, Info.price",
    }

    done = False
    start_key = None
    while not done:
        if start_key:
            scan_kwargs["ExclusiveStartKey"] = start_key
        response = table.scan(**scan_kwargs)
        print("Response:::", response)
        display_books(response.get("Items", []))
        start_key = response.get("LastEvaluatedKey", None)
        done = start_key is None


if __name__ == "__main__":

    def print_books(books):
        print("Scanned books:")
        for book in books:

            print(f"\n ISBN: {book['ISBN']} \n Title: {book['Title']}")
            pprint(book["Info"])

    query_range = (2019, 2021)  # (2019, 2021)
    print(f"Scanning for books published from {query_range[0]} to {query_range[1]}...")
    scan_books(query_range, print_books)
