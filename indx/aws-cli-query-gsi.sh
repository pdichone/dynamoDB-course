aws dynamodb query \
    --table-name Books \
    --index-name AuthorPriceIndex \
    --key-condition-expression "Author = :author" \
    --expression-attribute-values '{":author":{"S":"Author 34"}}' \
    --projection-expression "ISBN, Title, Author, Price, #yr, Info.subtitle, Info.authors, Info.short_description, Info.page_count, Info.categories" \
    --expression-attribute-names '{"#yr": "Year"}'
