import boto3
from decimal import Decimal
import json


def add_book():
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("Books")
    book = {
        "ISBN": "978-1-68050-153-0",
        "Year": 2017,
        "Title": "Deep Learning with TensorFlow",
        "Authors": ["Giancarlo Zaccone", "Md. Rezaul Karim"],
        "Price": Decimal("39.99"),
        "Category": "Technology",
        "Dimensions": "8.5 x 1.1 x 11 inches",
        "InPublication": True,
        "ProductCategory": "Book",
    }
    table.put_item(Item=book)
    return book


# def load_books(books, dynamodb=None):
#     if not dynamodb:
#         dynamodb = boto3.resource('dynamodb')

#     table = dynamodb.Table('Books')
#     for book in books:
#         isbn = book['title']
#         title = book['title']
#         print("Adding book:", isbn, title)
#         table.put_item(Item=book)

# if __name__ == '__main__':
#     with open("booksdata.json") as json_file:
#         book_list = json.load(json_file, parse_float=Decimal)
#     load_books(book_list)
if __name__ == "__main__":
    add_book()
    # with open("booksdata.json") as json_file:
    #     book_list = json.load(json_file, parse_float=Decimal)
    # load_books(book_list)
