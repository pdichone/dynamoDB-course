from decimal import Decimal
import json
import boto3

# === must pip install boto3 ===
# === run this script after running createTable.py to load a lot of books!===


def load_books(books, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("Books")
    for book in books:
        print(book["ISBN"], book["year"], book["title"])
        item = {
            "ISBN": book["ISBN"],  # ISBN is the partition key
            "Year": book["year"],
            "Title": book["title"],
            "Info": book["info"],
        }
        print("Adding book:", item["ISBN"], item["Title"])
        table.put_item(Item=item)


if __name__ == "__main__":
    with open("booksdata-final.json") as json_file:
        book_list = json.load(json_file, parse_float=Decimal)
    load_books(book_list)
