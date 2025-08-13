import os
import argparse
from logger import setup_logger

logger = setup_logger(__name__)

def load_config():
    parser = argparse.ArgumentParser()
    parser.add_argument("request_file", help="Request file to load from 'requests/' directory")
    parser.add_argument("attack_type", help="Type of attack to perform")
    args = parser.parse_args()

    attack = args.attack_type.lower()
    path = os.path.join("requests", args.request_file)
    logger.info(f"Loading request file from: {path}")

    with open(path, "r", encoding="utf-8") as f:
        raw_request = f.read()

    logger.debug(f"Loaded raw request: {raw_request[:100]}...")
    return raw_request, attack
