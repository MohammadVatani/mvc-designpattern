import logging
def setup_logging(name="logger",
                  filepath=None,
                  stream_log_level="DEBUG",
                  file_log_level="DEBUG"):
    
    logger = logging.getLogger(name)
    logger.setLevel("DEBUG")
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )    
    ch = logging.StreamHandler()
    ch.setLevel(getattr(logging, stream_log_level))
    ch.setFormatter(formatter)
    logger.addHandler(ch)    
    if filepath is not None:
        fh = logging.FileHandler(filepath)
        fh.setLevel(getattr(logging, file_log_level))
        fh.setFormatter(formatter)
        logger.addHandler(fh)    
    
    return logger
    
logger = setup_logging(name="default_log",filepath="logger.log")

def log_decorator(log_name="main"):
    def log_this(function):
        logger = logging.getLogger(log_name)
        def new_function(*args,**kwargs):
            try:
                output = function(*args,**kwargs)
                logger.debug(f"{function.__name__} - {args} - {kwargs}")
            except Exception as error:
                logger.error(f"{function.__name__}, error: {error}")
            return output
        return new_function
    return log_this