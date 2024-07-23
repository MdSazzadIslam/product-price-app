# Product-price-app

## Assignment

You are the new maintainer of a small Python web service that handles product
prices.

The service contains a set of products and aggregates prices from external
sources. A web application uses the service to display the prices to users.

You are tasked with implementing an API endpoint to display the products'
current prices and price trends.

The new API endpoint should work as follows:
```
GET http://localhost:8080/prices
```
```json
[
	{
		"product": "P001HYDRO",
		"price": 1.15,
		"currency": "EUR",
		"daily_change": "DOWN"
	},
	{
		"product": "P002SOLAR",
		"price": 1.28,
		"currency": "EUR",
		"daily_change": "SLIGHTLY UP"
	},
	// ...
]
```

You will need to retrieve a list of today's market prices from an external API:  
`GET http://localhost:8081/price-feed.json`.

- The response from the external API is a JSON list of price updates. Each valid
  price entry includes `product_id` (integer), `product_name` (string), `price`
  (number), and `updated_at` (datetime). All prices are expressed in EUR.

- The external API may return invalid price entries. You should ignore any price
  entries that do not include valid values for the aforementioned fields.

- Multiple price entries may exist for the same product. The first occurrence of
  a product represents its opening price today, while subsequent occurrences
  indicate price updates.

In your API's output, the `daily_change` should reflect the following logic:

- An increase of up to 5% is categorized as **SLIGHTLY UP**.
- An increase of more than 5% but less than or equal to 15% is categorized as
  **UP**.
- An increase of more than 15% is categorized as **SHARPLY UP**.
- A decrease of up to 5% is categorized as **SLIGHTLY DOWN**.
- A decrease of more than 5% but less than or equal to 15% is categorized as
  **DOWN**.
- A decrease of more than 15% is categorized as **SHARPLY DOWN**.

The increase/decrease is calculated as the percentage difference from the
opening price to the final price:
```
Price change = ((final price - opening price) / opening price) * 100
```
- The opening price is the first appearance of the product in the API response.
- The final price is the last appearance of the product in the API response.


### Bonus: Testing

The application lacks automated tests. Add unit tests for the new API endpoint
and any other parts of the application that you think should be tested.

Use the `pytest` framework for testing.


### Bonus: Monitoring

There is no monitoring set up. Propose metrics and alerts for the application. 
Use Prometheus or other solution of your choice.


## Running the application

### Alternative 1: Docker Compose

```sh
# Run the application and the "external" market prices API
docker compose up --build

# Run the tests
docker compose run app pytest -v
```

### Alternative 2: Python virtual environment

```sh
# Create a virtual environment with the app's dependencies
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

# Run the "external" market prices API in the background
python3 -m http.server -d external_api 8081 &

# Run the application
uvicorn product_price_app.main:app --port 8080 --reload
```
