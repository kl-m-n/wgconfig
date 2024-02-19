import os
import ipaddress

from utils import wg_install_path



def create_profile(name, subnet, port):
	# Generate paths
	directory = wg_install_path + "/profiles/" + name
	

	# Check if profiles directory exists
	if not os.path.isdir(wg_install_path + "/profiles"):
		os.mkdir(wg_install_path + "/profiles")

	# Check for duplicate ports
	taken_ports = set()
	for profile in os.listdir(wg_install_path + "/profiles"):
		for config_file in os.listdir(wg_install_path + "/profiles/" + profile):
			if config_file.endswith(".conf"):
				with open(wg_install_path + "/profiles/" + profile + "/" + config_file, "r") as config:
					for line in config:
						if line.startswith("ListenPort = "):
							taken_ports.add(int(line.split(" = ")[1].strip()))

	if int(port) in taken_ports:
		print("Port " + str(port) + " is already in use")
		exit(1)

	# If the profile already exists, exit
	if os.path.exists(directory + "/" + name + ".conf"):
		print("Profile already exists")
		exit(1)
	
	# Create a path
	if not os.path.exists(directory):
		os.makedirs(directory)

	# Create the private key
	os.system("wg genkey | tee " + directory + "/" + name + ".private | wg pubkey > " + directory + "/" + name + ".public")

	# Calculate the server's IP address
	ip = ipaddress.ip_network(subnet, strict=False)
	server_ip = str(ip.network_address + 1)

	# Create the configuration file
	with open(directory + "/" + name + ".conf", "w") as config:
		config.write("[Interface]\n")
		config.write("# Subnet = " + subnet + "\n")
		config.write("Address = " + server_ip + "/32\n")
		config.write("ListenPort = " + str(port) + "\n")
		with open(directory + "/" + name + ".private", "r") as key_file:
			config.write("PrivateKey = " + key_file.read())
		config.write("\n")