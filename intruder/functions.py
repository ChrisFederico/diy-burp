import requests
from logger import setup_logger

logger = setup_logger(__name__)
session = requests.Session()

def parse_raw_request(raw_request):
    lines = raw_request.split("\n")
    method, path, _ = lines[0].split()
    headers = {}
    body = ""
    is_body = False

    for line in lines[1:]:
        if line.strip() == "":
            is_body = True
            continue
        if is_body:
            body += line
        else:
            key, value = line.split(":", 1)
            headers[key.strip()] = value.strip()

    return method, path, headers, body


def send_request(method, url, headers, body):
    if method == "POST":
        return session.post(url, headers=headers, data=body)
    elif method == "GET":
        return session.get(url, headers=headers, verify=False)
    else:
        raise ValueError(f"Unsupported HTTP method: {method}")
