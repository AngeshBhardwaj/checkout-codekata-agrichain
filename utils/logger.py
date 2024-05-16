import logging

# creating a logger object named 'checkout_app_logger'
logger = logging.getLogger('checkout_app_logger')
logger.setLevel(logging.INFO)

# Create handlers
f_handler = logging.FileHandler('./logs/app.log')

# Create formatters and add it to handlers
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(f_handler)
