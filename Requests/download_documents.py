import requests

server = 'http://127.0.0.1:8000/' 
url = server + 'api/' 
customer_id = 9 

graphql_query = '''
query GetDocuments($customerId: Int!) {
  documents(customerId: $customerId)
}
'''
variables = {
    "customerId": customer_id
}

response = requests.post(url, json={'query': graphql_query, 'variables': variables})
data = response.json()
document_urls = data.get('data', {}).get('documents')

if document_urls:
    for index, url in enumerate(document_urls, start=1):
        response = requests.get(server + url)
        if response.status_code == 200:
            content_type = response.headers.get('content-type')
            file_extension = content_type.split('/')[-1]
            file_name = f"document_{index}.{file_extension}"
            with open(file_name, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {file_name}")
        else:
            print(f"Failed to download document {index}.")
else:
    print("No documents found for the given customer ID.")