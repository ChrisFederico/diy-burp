from config import load_config
from functions import parse_raw_request, send_request, load_payloads, load_multiple_payload_lists
from logger import setup_logger
import re
import itertools

logger = setup_logger(__name__)

def main():
    raw_request, attack = load_config()

    method, path, headers, body_template = parse_raw_request(raw_request)
    base_url = f"https://{headers['Host']}{path}"
    
    if attack == "sniper":
        payloads = load_payloads("list.txt")
        logger.info(f"Starting scan on: {base_url}")
        for payload in payloads:
            body = body_template.replace("§payload§", payload)
            response = send_request(method, base_url, headers, body)
            logger.info(f"[{payload}] → Status: {response.status_code}, Length: {len(response.text)}")
    elif attack == "clusterbomb":
        payload_lists, files = load_multiple_payload_lists()
        logger.info(f"Starting cluster bomb scan on: {base_url}")
        markers = re.findall(r"§(payload\d+)§", body_template)
        if not markers:
            logger.error("No payload markers found in request template for cluster bomb attack.")
            return
        if len(markers) != len(payload_lists):
            logger.error(f"Number of payload markers ({len(markers)}) does not match number of payload lists ({len(payload_lists)}).")
            return
        for combo in itertools.product(*payload_lists):
            body = body_template
            for marker, payload in zip(markers, combo):
                body = body.replace(f"§{marker}§", payload)
            response = send_request(method, base_url, headers, body)
            logger.info(f"[{combo}] → Status: {response.status_code}, Length: {len(response.text)}")

    else:
        logger.error(f"Unknown attack type: {attack}. Supported types are 'sniper' and 'clusterbomb'.")

if __name__ == "__main__":
    main()
