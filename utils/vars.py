from configparser import ConfigParser
import logging
from datetime import datetime

# Defaults
config = ConfigParser()
config.read('/etc/wgconfig/config/config.ini')

current_date = datetime.now()

# Get the root logger
logger = logging.getLogger()

# Define a handler that writes INFO messages or higher to the sys.stderr (console)
console = logging.StreamHandler()
console.setLevel(logging.INFO)

# Define a format for your logs
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Add the format/structure to your handler
console.setFormatter(formatter)

# Add the console handler to your logger (this is what directs the messages to the console) - Uncomment to enable console logging
# logger.addHandler(console)

# Wireguard configuration
wg_install_path = config.get('Wireguard', 'InstallPath')