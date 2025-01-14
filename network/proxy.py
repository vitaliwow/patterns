import requests

def main() -> dict:
    auth_name = ""
    auth_pass = ""
    proxy = ""
    port = 8888
    response = requests.get(
        "https://api.openai.com",
        proxies={
            "http": f"http://{auth_name}:{auth_pass}@{proxy}:{port}"
        }
    )
    return response.json()


if __name__ == "__main__":
    response = main()

    print(response)