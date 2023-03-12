import requests

# Get amount and currencies from user
amount = float(input("Enter amount to convert: "))
from_currency = input("Enter currency to convert from: ").upper()
to_currency = input("Enter currency to convert to: ").upper()

# Define API endpoint and parameters
endpoint = "https://api.exchangeratesapi.io/latest"
params = {'base': from_currency, 'symbols': to_currency}

# Make request to API
response = requests.get(endpoint, params=params)

# Parse exchange rate from response
exchange_rate = response.json()['rates'][to_currency]

# Convert amount to target currency
converted_amount = amount * exchange_rate

# Print result
print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
