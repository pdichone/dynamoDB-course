aws dynamodb update-table ^
    --table-name Books ^
    --attribute-definitions ^
        AttributeName=Author,AttributeType=S ^
        AttributeName=Price,AttributeType=N ^
    --global-secondary-index-updates ^
        "[ ^
            { ^
                \"Create\": { ^
                    \"IndexName\": \"AuthorPriceIndex\", ^
                    \"KeySchema\": [ ^
                        {\"AttributeName\": \"Author\", \"KeyType\": \"HASH\"}, ^
                        {\"AttributeName\": \"Price\", \"KeyType\": \"RANGE\"} ^
                    ], ^
                    \"Projection\": { ^
                        \"ProjectionType\": \"ALL\" ^
                    }, ^
                    \"ProvisionedThroughput\": { ^
                        \"ReadCapacityUnits\": 10, ^
                        \"WriteCapacityUnits\": 10 ^
                    } ^
                } ^
            } ^
        ]"
