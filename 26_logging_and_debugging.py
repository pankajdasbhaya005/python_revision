# Logging and Debugging in Python
# Logging is used to track events, errors and debugging information


# 1. Basic logging setup
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")

# Output (example):
# DEBUG:root:This is debug message
# INFO:root:This is info message
# WARNING:root:This is warning message
# ERROR:root:This is error message
# CRITICAL:root:This is critical message


# 2. Logging levels
# DEBUG < INFO < WARNING < ERROR < CRITICAL

# If level = WARNING
# Only WARNING and above will show


# 3. Logging to a file
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logging.info("Application started")
logging.warning("Low disk space")

# Output:
# (Messages saved in app.log file)



# 4. Using logger object (better practice)
logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
formatter = logging.Formatter("%(levelname)s %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.debug("Debugging mode on")
logger.error("Something went wrong")

# Output:
# DEBUG Debugging mode on
# ERROR Something went wrong




# 5. Debugging using assert
x = 10
y = 5

assert x > y, "x should be greater than y"

# If false> AssertionError


# 6. Using pdb (Python debugger)
# Uncomment to use interactive debugger

# import pdb
# pdb.set_trace()

# This pauses execution and allows stebstep debugging


# 7. Logging exception details
try:
    result = 10 / 0
except Exception as e:
    logging.exception("Exception occurred")

# Output:
# ERROR:root:Exception occurred
# Traceback (most recent call last):
# ZeroDivisionError: division by zero
