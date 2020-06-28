import logging


def get_logger(name):
    logger = logging.getLogger(name)
    logger.addHandler(stream_handler)
    logger.setLevel(getattr(logging, 'DEBUG'))

    # if settings.LOGFILE is not None:
    #     logger.addHandler(file_handler)

    # logger.debug("Logging initialized")
    return logger


# if settings.DEBUG:
fmt = logging.Formatter("%(asctime)s %(levelname)s # %(message)s")
# else:
#     fmt = logging.Formatter("%(asctime)s %(levelname)s %(name)s # %(message)s")

# if settings.LOGFILE is not None:
#     file_handler = logging.FileHandler(os.path.join(settings.LOGDIR, settings.LOGFILE))
#     file_handler.setFormatter(fmt)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(fmt)
