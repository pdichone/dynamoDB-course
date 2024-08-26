aws dynamodb query ^
    --table-name Books ^
    --index-name PriceIndex ^
    --key-condition-expression "ISBN = :isbn AND Price BETWEEN :min_price AND :max_price" ^
    --expression-attribute-values "{\":isbn\":{\"S\":\"28cf5e8d-9965-453f-b8bf-ba28ce92f443\"}, \":min_price\":{\"N\":\"10\"}, \":max_price\":{\"N\":\"50\"}}" ^
    --projection-expression "ISBN, Title, Price, #yr, Info.subtitle, Info.authors, Info.short_description, Info.page_count, Info.categories" ^
    --expression-attribute-names "{ \"#yr\": \"Year\" }"
