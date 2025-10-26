# DAY 26

API stands for "Application Programming Interface." In simple terms, it's a set of rules and protocols that allow how different software applications can communicate and interact with each other.

## Python API

In order to work with APIs, some tools are required, such as requests module and we need to first install them in our system.

### Command to install 'requests'

-        `pip install requests`

Once we have installed it, we need to import it in our code to use it.

### Sample "POST" request code:

```python
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
```
