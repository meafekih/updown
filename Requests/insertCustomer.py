import requests
import base64

url = 'http://127.0.0.1:8000/api/' 

mutation = '''
mutation insertCustomer(
  $name: String!,
  $email: String!,
  $fileNames: [String],
  $files: [String]
) {
  insertCustomer(
    name: $name,
    email: $email,
    fileNames: $fileNames,
    files: $files
  ) {
    customer {
      id
      name
      email
    }
  }
}
'''

file_names = ["c.pdf", "d.png"]

variables = {
    'name': 'John',
    'email': 'John@example.com',
    'fileNames': file_names,
    'files': []
}

for file_name in file_names:
    with open('docs/' + file_name, 'rb') as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')
        variables['files'].append(image_data)

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