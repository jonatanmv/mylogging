import logging 
from MyLogging import MyLog

log = MyLog.get_logger(
	name=__file__,
	log_level=logging.DEBUG,
)

log.debug("Hello. This is a test. Thanks !")
