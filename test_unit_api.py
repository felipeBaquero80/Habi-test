import json
import http.client

host = "localhost"
port = 8080


def test_get():
    """
    Send a GET request to the specified host and port.

    Returns:
        tuple: A tuple containing the HTTP status code and the response data.
    """
    conn = http.client.HTTPConnection(host, port)
    conn.request("GET", "/")

    response = conn.getresponse()
    status_code = response.status
    response_data = response.read().decode('utf-8')

    conn.close()

    return status_code, response_data


def test_post(data):
    """
    Send a POST request with JSON data to the specified host and port.

    Args:
        data (dict): JSON data to be sent in the request body.

    Returns:
        tuple: A tuple containing the HTTP status code and the response data.
    """
    conn = http.client.HTTPConnection(host, port)
    headers = {"Content-type": "application/json"}
    json_data = json.dumps(data)
    conn.request("POST", "/filtros", body=json_data, headers=headers)

    response = conn.getresponse()
    status_code = response.status
    response_data = response.read().decode('utf-8')

    conn.close()

    return status_code, response_data

status_code, response_data = test_get()
print(f"GET Response: Status Code {status_code}, Data: {response_data}")

# test
data = {
    "filter_city": "medellin",
    "filter_address": "",
    "filter_year": "2011"
}
status_code, response_data = test_post(data)
print(f"POST Response: Status Code {status_code}, Data: {response_data}")
