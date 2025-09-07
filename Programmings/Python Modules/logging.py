""" 
Logging : 
1. It provides a way to track events, errors and operation information of any application.
2. It is build-in logging module offers a flexible framework for emitting log messages from python programs.
3. how to configure logging, log levels and best practices for using logging in python applications.

Python logging module has several log levels indicating the severity of events and default levels are 
1. DEBUG: Detailed information, typically of interest only when diagnosing problems.
2. INFO: Confirmation that things are working as expected.
3. WARNING: An indication that something unexpected happened or indicative of some problem in the near future (e.g., ‘disk space low’). The software is still working as expected.
4. ERROR: Due to a more serious problem, the software has not been able to perform some function.
5. CRITICAL: A very serious error, indicating that the program itself may be unable to continue running.

"""
#%% dependencies
import logging

#%% Configure the basic logging settings
logging.basicConfig(level=logging.DEBUG)

# log messages with different severity levels
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

#%% configuring logging
logging.basicConfig(
    filename='logging/app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


# log messages with different severity levels
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

#%% Logging with Multiple Loggers
# How to create multiple loggers for different parts of your application.

logger1 = logging.getLogger("module1")
logger1.setLevel(logging.DEBUG)

# creating a logger for module 2
logger2 = logging.getLogger("module2")
logger2.setLevel(logging.WARNING)

# configure logging setting
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
) # log message with different loggers
logger1.debug("This is debug message for module1")
logger2.warning("This is a warning message for module 2")
logger2.error("This is an error message")