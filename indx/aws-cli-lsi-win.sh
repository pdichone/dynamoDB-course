aws dynamodb create-table ^
    --table-name Books ^
    --attribute-definitions ^
        AttributeName=ISBN,AttributeType=S ^
        AttributeName=Year,AttributeType=N ^
        AttributeName=Price,AttributeType=N ^
    --key-schema ^
        AttributeName=ISBN,KeyType=HASH ^
        AttributeName=Year,KeyType=RANGE ^
    --local-secondary-indexes ^
        "[ ^
            { ^
                \"IndexName\": \"PriceIndex\", ^
                \"KeySchema\": [ ^
                    {\"AttributeName\": \"ISBN\", \"KeyType\": \"HASH\"}, ^
                    {\"AttributeName\": \"Price\", \"KeyType\": \"RANGE\"} ^
                ], ^
                \"Projection\": { ^
                    \"ProjectionType\": \"ALL\" ^
                } ^
            } ^
        ]" ^
    --provisioned-throughput ReadCapacityUnits=10,WriteCapacityUnits=10
