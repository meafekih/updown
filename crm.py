import requests
import base64

url = 'http://127.0.0.1:8000/api/' 

mutation = '''
mutation insertCustomer(
  $name: String!,
  $email: String!,
) {
  insertCustomer(
    name: $name,
    email: $email,
  ) {
    customer {
      id
      name
      email
    }
  }
}
'''


variables = {
    'name': 'John',
    'email': 'John@example.com',
}

request_payload = {
    'query': mutation,
    'variables': variables,
}

response = requests.post(url, json=request_payload)

if response.status_code == 200:
    data = response.json()
    print(data)
    customer = data['data']['insertCustomer']['customer']
    print(f"Customer ID: {customer['id']}, Name: {customer['name']}")
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)
