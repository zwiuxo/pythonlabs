import requests
import json

url = "https://httpbin.org"
get_endpoint = "/get"
post_endpoint = "/post"

def print_response(resp, method_name):
    print(f"\n==== {method_name} RESPONSE ====")
    print("Status Code:", resp.status_code)
    print("Headers:")
    for k, v in resp.headers.items():
        print(f"  {k}: {v}")
    print("Body:\n", resp.text)
    print("=" * 40)


print("==== OPTIONS REQUEST ====")
resp_options = requests.options(url)
print_response(resp_options, "OPTIONS")


params = {"param1": "value1", "param2": "value2"}
get_url = url + get_endpoint
print("\n==== GET REQUEST ====")
print("GET URL:", get_url)
print("Params:", params)
resp_get = requests.get(get_url, params=params)
print_response(resp_get, "GET")


post_data = {"username": "test_user", "password": "12345"}
headers = {'Content-Type': 'application/json'}
post_url = url + post_endpoint
print("\n==== POST REQUEST ====")
print("POST URL:", post_url)
print("Payload (JSON):", json.dumps(post_data))
resp_post = requests.post(post_url, data=json.dumps(post_data), headers=headers)
print_response(resp_post, "POST")