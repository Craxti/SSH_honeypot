# utils/logger.py
import logging
from utils.config import LOG_FILE

logging.basicConfig(filename=LOG_FILE, level=logging.INFO)
logger = logging.getLogger(__name__)
