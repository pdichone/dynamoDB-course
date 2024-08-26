from decimal import Decimal
import json
import boto3

# === must pip install boto3 ===
# === run this script after running create_books_table_with_lsi.py to load books! ===


def load_books(books, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("Books")
    for book in books:
        print(book["ISBN"], book["Year"], book["Title"])
        # Extract the first author for the Author attribute
        author = book["Info"]["authors"][0] if book["Info"]["authors"] else "Unknown"
        item = {
            "ISBN": book["ISBN"],  # ISBN is the partition key
            "Year": book["Year"],  # Year is the sort key
            "Title": book["Title"],
            "Price": book["Price"],
            "Author": author,
            "Info": book["Info"],
        }
        print("Adding book:", item["ISBN"], item["Title"])
        table.put_item(Item=item)


if __name__ == "__main__":
    with open("restructured-booksdata.json") as json_file:
        book_list = json.load(json_file, parse_float=Decimal)
    load_books(book_list)


# from decimal import Decimal
# import json
# import boto3

# # === must pip install boto3 ===
# # === run this script after running create_books_table_with_lsi.py to load books! ===


# def load_books(books, dynamodb=None):
#     if not dynamodb:
#         dynamodb = boto3.resource("dynamodb")

#     table = dynamodb.Table("Books")
#     for book in books:
#         print(book["ISBN"], book["Year"], book["Title"])
#         item = {
#             "ISBN": book["ISBN"],  # ISBN is the partition key
#             "Year": book["Year"],  # Year is the sort key
#             "Title": book["Title"],
#             "Price": book["Price"],
#             "Info": book["Info"],
#         }
#         print("Adding book:", item["ISBN"], item["Title"])
#         table.put_item(Item=item)


# if __name__ == "__main__":
#     with open("restructured-booksdata.json") as json_file:
#         book_list = json.load(json_file, parse_float=Decimal)
#     load_books(book_list)
