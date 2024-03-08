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
wg_persistent_peers = config.get('Wireguard', 'PersistentPeers')

# Mail configuration
mail_status = config.get('Mail', 'Mail')
mail_server = config.get('Mail', 'Server')
mail_port = config.get('Mail', 'Port')
mail_username = config.get('Mail', 'Username')
mail_password = config.get('Mail', 'Password')
mail_from = config.get('Mail', 'From')