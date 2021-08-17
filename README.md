# retail-calculator
kind calculator Ѷ


# Create '.env' file in root and set variables as below:
```
DB_URI=postgresql+asyncpg://test:test@db:5432/test
POSTGRES_USER=test
POSTGRES_DB=test
POSTGRES_PASSWORD=test
```

# Run app locally
```
poetry install
export DB_URI=...
python -m retail_calculator.app
```

# Run linter
```
flakehell lint ./src/ & flakehell lint ./tests/
```

# Run tests: make sure db exists
```
export DB_URI=...
pytest
```

# Run app as docker compose
```
docker-compose up
```

# API example
```
curl --location --request POST 'http://0.0.0.0:8000/v1/orders' \
--header 'Content-Type: application/json' \
--data-raw '{
    "product_amount": 2,
    "price_per_product": 1000.99,
    "state": "UT"
}'
```
