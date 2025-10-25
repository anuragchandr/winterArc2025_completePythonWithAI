# DAY 25

API stands for "Application Programming Interface." In simple terms, it's a set of rules and protocols that allow how different software applications can communicate and interact with each other.

## Python API

In order to work with APIs, some tools are required, such as requests module and we need to first install them in our system.

### Command to install 'requests'

-        `pip install requests`

Once we have installed it, we need to import it in our code to use it.

### Command to import 'requests':

- `import requests`

## Common HTTP Request Methods

| **Method** | **Definition** |
|------------|----------------|
| `GET`      | Retrieves data from the server. It’s read-only and doesn’t change server state. |
| `POST`     | Sends data to the server to create a new resource. Often used for form submissions. |
| `PUT`      | Replaces the entire resource at the target URL with the data provided. |
| `PATCH`    | Updates part of a resource. More efficient than `PUT` when only a few fields change. |
| `DELETE`   | Removes the specified resource from the server. |
| `HEAD`     | Same as `GET`, but only returns headers (no body). Useful for checking metadata. |
| `OPTIONS`  | Describes the communication options available for the target resource. |
| `TRACE`    | Performs a diagnostic loop-back test to see how a request travels to the server. |
| `CONNECT`  | Establishes a tunnel to the server, typically used for HTTPS via a proxy. |

### example

```python 
import requests

# API endpoint
url = "http://api.open-notify.org/astros.json"

# Send GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print("Number of astronauts in space:", data["number"])
    for person in data["people"]:
        print(f"{person['name']} is on the {person['craft']}")
else:
    print("Failed to retrieve data. Status code:", response.status_code)

```

## Understanding API Status Codes

### Status codes tell us how the server handled our request

- __200 OK__: Request successful, data returned.
- **201 Created**: New resource created.
- **204 No Content**: Success but no data returned.
- **400 Bad Request**: Invalid request.
- **401 Unauthorized**: Missing or invalid API key.
- **500 Internal Server Error**: Server encountered an error.

! _Here we learn only requesting API Handling and not API dvelopment using python._
