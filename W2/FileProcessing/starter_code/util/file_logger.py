import logging

def setup_logger(name):

    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.WARNING)
        handler = logging.FileHandler("app.log", mode="a", encoding="utf-8")
        formatter = logging.Formatter(
            '%(asctime)s | %(name)s | %(levelname)s | %(message)s',
            datefmt = '%H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
