from config import load_config
from functions import parse_raw_request, send_request
from logger import setup_logger
import os

logger = setup_logger(__name__)

def load_payloads(file_path):
    path = os.path.join("payloads", file_path)
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def main():
    raw_request, attack = load_config()

    payloads = load_payloads("list.txt")
    method, path, headers, body_template = parse_raw_request(raw_request)
    base_url = f"https://{headers['Host']}{path}"
    
    if attack == "sniper":
        logger.info(f"Starting scan on: {base_url}")
        for payload in payloads:
            body = body_template.replace("§payload§", payload)
            response = send_request(method, base_url, headers, body)
            logger.info(f"[{payload}] → Status: {response.status_code}, Length: {len(response.text)}")
    elif attack == "clusterbomb":
        logger.error("Cluster bomb attack is not yet implemented.")
    else:
        logger.error(f"Unknown attack type: {attack}. Supported types are 'sniper' and 'clusterbomb'.")

if __name__ == "__main__":
    main()
