# create-table
aws dynamodb create-table ^
    --table-name Books ^
    --attribute-definitions AttributeName=ISBN,AttributeType=S ^
    --key-schema AttributeName=ISBN,KeyType=HASH ^
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5

# verify table
aws dynamodb describe-table --table-name Books

# insert item
aws dynamodb put-item ^
    --table-name Books ^
    --item "{\"ISBN\": {\"S\": \"978-3-16-148410-0\"}, \"Title\": {\"S\": \"Example Book\"}, \"Author\": {\"S\": \"John Doe\"}, \"Price\": {\"N\": \"19.99\"}}"

aws dynamodb put-item ^
    --table-name Books ^
    --item "{\"ISBN\": {\"S\": \"978-1-40-289462-3\"}, \"Title\": {\"S\": \"Another Book\"}, \"Author\": {\"S\": \"Jane Smith\"}, \"Price\": {\"N\": \"29.99\"}}"

aws dynamodb put-item ^
    --table-name Books ^
    --item "{\"ISBN\": {\"S\": \"978-0-12-345678-9\"}, \"Title\": {\"S\": \"More Examples\"}, \"Author\": {\"S\": \"Alice Johnson\"}, \"Price\": {\"N\": \"39.99\"}}"

# get item
aws dynamodb query ^
    --table-name Books ^
    --key-condition-expression "ISBN = :isbn" ^
    --expression-attribute-values "{\":isbn\": {\"S\": \"978-3-16-148410-0\"}}"

# scan table
aws dynamodb scan --table-name Books

# update item
aws dynamodb update-item ^
    --table-name Books ^
    --key "{\"ISBN\": {\"S\": \"978-3-16-148410-0\"}}" ^
    --update-expression "SET Price = :newPrice" ^
    --expression-attribute-values "{\":newPrice\": {\"N\": \"24.99\"}}"

# delete item
aws dynamodb delete-item ^
    --table-name Books ^
    --key "{\"ISBN\": {\"S\": \"978-3-16-148410-0\"}}"

# delete table
aws dynamodb delete-table --table-name Books