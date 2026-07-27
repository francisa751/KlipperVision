from klippervision.utils.logger import setup_logger


def main():
    logger = setup_logger()

    logger.info("KlipperVision starting...")
    logger.info("Logger initialized successfully")


if __name__ == "__main__":
    main()