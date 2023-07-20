""" 
initiates a logger for the API. 
The script configures the logger with environmental variables. 
"""
import os
import logging

LOG_LEVEL = os.getenv("LOG_LEVEL", "ERROR")
LOG_FILE = os.getenv("LOG_FILE", None)

logger = logging.getLogger("categorization_api_logger")

log_level_lookup = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}

logger.setLevel(log_level_lookup.get(LOG_LEVEL, "ERROR"))

formatter = logging.Formatter(
    "%(levelname)s - %(asctime)s - %(message)s"
)

if LOG_FILE:
    if not os.path.exists("logs"):
        os.makedirs("logs")

    file_handler = logging.FileHandler(f"logs/{LOG_FILE}")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

else:
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

