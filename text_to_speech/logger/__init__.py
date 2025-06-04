import logging
import os
from datetime import datetime

LOG_DIR = 'pylogs'
LOG_DIR_PATH = os.path.join(os.getcwd(), LOG_DIR)

os.makedirs(LOG_DIR, exist_ok=True)

CURRENT_TIME_STAMP = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
file_name = f"log{CURRENT_TIME_STAMP}"
log_file_path = os.path.join(LOG_DIR, file_name)

logging.basicConfig(level = logging.INFO,
                    filename=log_file_path)
