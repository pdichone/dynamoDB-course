import json

# Load the original data
with open('booksdata-final.json', 'r') as file:
    books = json.load(file)

# Restructure the data
restructured_books = []
for book in books:
    restructured_book = {
        "ISBN": book["ISBN"],
        "Title": book["title"],
        "Year": book["year"],
        "Price": book["info"]["price"],
        "Info": {
            "subtitle": book["info"]["subtitle"],
            "authors": book["info"]["authors"],
            "short_description": book["info"]["short_description"],
            "page_count": book["info"]["page_count"],
            "categories": book["info"]["categories"]
        }
    }
    restructured_books.append(restructured_book)

# Save the restructured data to a new file
output_path = 'restructured_booksdata.json'
with open(output_path, 'w') as file:
    json.dump(restructured_books, file, indent=4)

print(f'Restructured data saved to {output_path}')
