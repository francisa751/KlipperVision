from loguru import logger
import sys


def setup_logger():
    logger.remove()

    logger.add(
        sys.stdout,
        level="INFO",
        colorize=True,
        format="<green>{time:HH:mm:ss}</green> | "
               "<level>{level}</level> | "
               "{message}",
    )

    logger.add(
        "logs/klippervision.log",
        rotation="10 MB",
        retention="30 days",
        level="DEBUG",
    )

    return logger