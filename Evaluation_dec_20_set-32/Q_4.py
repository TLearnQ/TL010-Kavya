import requests

url = "https://httpbin.org/delete"
token = "mytoken"

headers = {
    "Authorization": f"Bearer {token}"
}

try:
    response = requests.delete(url, headers=headers, timeout=5)

    if response.status_code == 200:
        data = response.json()

       
        auth_header = data.get("headers", {}).get("Authorization")

        if auth_header == f"Bearer {token}":
            print("SUCCESS: Authorization header verified")
        else:
            print("FAILURE: Authorization header not found")

    else:
        print(f"FAILURE: HTTP status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print("ERROR: Request failed")
    print(e)
