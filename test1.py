from src.textSummarizer.logging import logger

logger.info("Logging has started for the text summarization process.")

try:
    a = 1 / 0
except Exception as e:
    logger.info("An error occurred: {}".format(e))