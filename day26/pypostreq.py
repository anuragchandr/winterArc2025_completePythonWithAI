import requests

# Define the URL
url = 'https://httpbin.org/post'

# Define the data to be sent in the request body
data = {'key1': 'value1', 'key2': 'value2'}

# Send the POST request with the data
response = requests.post(url, data=data)

# Print the response status code
print('Status Code:', response.status_code)

# Print the response content
print('Response Content:', response.text)