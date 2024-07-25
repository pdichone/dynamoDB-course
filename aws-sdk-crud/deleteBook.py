import boto3
from boto3.dynamodb.conditions import Key, Attr


def delete_book(title=None, isbn=None, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("Books")

    # Query the table to find the item based on title or ISBN
    if isbn:
        response = table.query(KeyConditionExpression=Key("ISBN").eq(isbn))
    elif title:
        response = table.scan(FilterExpression=Attr("Title").eq(title))
    else:
        raise ValueError("Either title or ISBN must be provided.")

    items = response.get("Items", [])

    if not items:
        print("No book found with the given title or ISBN.")
        return

    # Assume we delete the first matched item
    item_to_delete = items[0]

    # Delete the item
    table.delete_item(
        Key={"ISBN": item_to_delete["ISBN"], "Year": item_to_delete["Year"]}
    )
    print(
        f"Deleted book with ISBN: {item_to_delete['ISBN']} and Title: {item_to_delete['Title']}"
    )


if __name__ == "__main__":
    # Example usage
    # delete_book(title="Sample Book Title 57")
    delete_book(isbn="7477f9b8-d046-42b1-a158-90fb4c6387c2")
