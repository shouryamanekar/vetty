# Vetty SDE – Python API Technical Exercise

## Description
This project is an HTTP REST API that fetches cryptocurrency market updates from the CoinGecko API.

## Endpoints
- `/coins`: List all coins.
- `/categories`: List coin categories.
- `/coins/<coin_id>`: List specific coin by ID.
- `/health`: Health check endpoint.
- `/version`: Version information endpoint.

## How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set the API key: `export API_KEY="your_api_key_here"`.
4. Run the application: `python app.py`.

## Docker
1. Build the Docker image: `docker build -t vetty-api .`.
2. Run the Docker container: `docker run -p 5000:5000 vetty-api`.

## Tests
Run tests with: `pytest`.

## Authentication
The application uses an API key for authentication. Ensure to include the API key in the request headers.

## Linting
Lint the code with: `flake8`.

## Version
1.0.0
