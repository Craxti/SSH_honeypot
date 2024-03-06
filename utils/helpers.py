# utils/helpers.py
import json
from utils.logger import logger

def log_action(action, username, ip_address, command):
    log_entry = {
        'action': action,
        'username': username,
        'ip_address': ip_address,
        'command': command
    }
    logger.info(json.dumps(log_entry))
