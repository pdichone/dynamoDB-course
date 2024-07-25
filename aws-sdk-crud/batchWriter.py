import boto3
from decimal import Decimal
import json


# An example use case of batch writer to add multiple books to the table
# in this case, we are adding books from a JSON file (this is just an example and the file is not provided)
# The JSON file should contain a list of books with the following structure:
# [ { "year": 2010, "title": "Book Title", "info": { "subtitle": "Book Subtitle", "author": "Author Name" } }, ... ]
def batch_write_books(books, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("Books")
    with table.batch_writer() as batch:
        for book in books:
            # Add a unique ISBN to each book if not present
            if "ISBN" not in book:
                book["ISBN"] = str(uuid.uuid4())

            # Ensure the item structure matches the table schema
            item = {
                "ISBN": book["ISBN"],
                "Year": book["year"],
                "Title": book["title"],
                "Info": book["info"],
            }
            batch.put_item(Item=item)
            print(f"Added book: {item['ISBN']} - {item['Title']}")


if __name__ == "__main__":
    # Load books from JSON file
    with open("updated_booksdata_with_proper_titles.json") as json_file:
        book_list = json.load(json_file, parse_float=Decimal)

    # Perform batch write
    batch_write_books(book_list)
