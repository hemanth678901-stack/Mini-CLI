import logging
from pathlib import Path

# Setting up the basic config.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler("System.log")
formatter = logging.Formatter("%(asctime)s - %(message)s - %(error)s")
handler.setFormatter(formatter)

directory = Path("data")

# A class for custom exception.
class EmptyContentError(Exception):
    def __init__(self, message):
        # Initialize the base exception with custom error message.
        super().__init__(message)

def write_file(directory , filename: str, content: str):
    if len(content) == 0:
        raise EmptyContentError("The content is empty.")
    directory.mkdir(parents=True, exist_ok=True)
    full_path = directory / filename
    full_path.write_text(content)
    logger.info("Data added successfully.")
try:
    write_file(directory, "config.json", "")
except EmptyContentError as e:
    logger.error(e)