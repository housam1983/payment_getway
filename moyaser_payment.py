import requests

# Replace with your Moyasar API key
API_KEY = 'sk_test_your_api_key'

PAYMENT_URL = 'https://api.moyasar.com/v1/payments'

payload = {
    'amount': 1000,  # Amount in the smallest currency unit (e.g., halalas)
    'currency': 'SAR',
    'description': 'Test payment',
    'callback_url': 'https://example.com/callback',
    'source': {
        'type': 'creditcard',
        'name': 'John Doe',
        'number': '4111111111111111',
        'month': '12',
        'year': '2025',
        'cvc': '123'
    }
}

response = requests.post(
    PAYMENT_URL,
    auth=(API_KEY, ''),
    json=payload
)

print('Status:', response.status_code)
print('Response:', response.json())
