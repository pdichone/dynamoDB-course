aws dynamodb create-table \
    --table-name Books \
    --attribute-definitions \
        AttributeName=ISBN,AttributeType=S \
        AttributeName=Year,AttributeType=N \
        AttributeName=Author,AttributeType=S \
        AttributeName=Price,AttributeType=N \
    --key-schema \
        AttributeName=ISBN,KeyType=HASH \
        AttributeName=Year,KeyType=RANGE \
    --global-secondary-indexes \
        "[
            {
                \"IndexName\": \"AuthorPriceIndex\",
                \"KeySchema\": [
                    {\"AttributeName\": \"Author\", \"KeyType\": \"HASH\"},
                    {\"AttributeName\": \"Price\", \"KeyType\": \"RANGE\"}
                ],
                \"Projection\": {
                    \"ProjectionType\": \"ALL\"
                },
                \"ProvisionedThroughput\": {
                    \"ReadCapacityUnits\": 10,
                    \"WriteCapacityUnits\": 10
                }
            }
        ]" \
    --provisioned-throughput ReadCapacityUnits=10,WriteCapacityUnits=10
