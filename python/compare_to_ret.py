#接收多个参数拼接url
def test(*args):
    url = 'www.1.com'
    for i in args:
        url += i + ','
    return url




import logzero
from logzero import logger

# Setup rotating logfile with 3 rotations, each with a maximum filesize of 1MB:
logzero.logfile("rotating-logfile.log", maxBytes=1e6, backupCount=3)

# Log messages
logger.info("This log message goes to the console and the logfile!")