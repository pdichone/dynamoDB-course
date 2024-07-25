import boto3
from boto3.dynamodb.conditions import Key, Attr


def update_book_subtitle(new_subtitle, title=None, isbn=None, dynamodb=None):
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

    # Assume we update the first matched item
    item_to_update = items[0]

    # Update the subtitle
    table.update_item(
        Key={"ISBN": item_to_update["ISBN"], "Year": item_to_update["Year"]},
        UpdateExpression="set Info.subtitle = :s",
        ExpressionAttributeValues={":s": new_subtitle},
        ReturnValues="UPDATED_NEW",
    )
    print(
        f"Updated book with ISBN: {item_to_update['ISBN']} and Title: {item_to_update['Title']} with new subtitle: {new_subtitle}"
    )


if __name__ == "__main__":
    # Example usage
    # update_book_subtitle(new_subtitle="A New Sci-Fi Adventure", title="The Quantum Thief")
    update_book_subtitle(
        new_subtitle="An Updated Psychological Thriller",
        isbn="f542df42-acd5-4290-9d0f-ae1aeafe8de6",
    )
