import os
import ipaddress

from utils import wg_install_path
from utils.get_server_ip import get_server_ip



def create_group(name, profile, subnet):
	# Profile directory
	profile_directory = wg_install_path + "/profiles/" + profile

	# Check if the profile exists
	if not os.path.exists(profile_directory):
		print("Profile does not exist")
		exit(1)

	# Create the groups directory
	if not os.path.isdir(profile_directory + "/groups"):
		os.mkdir(profile_directory + "/groups")

	# Check if the group already exists
	if os.path.isfile(profile_directory + "/groups/" + name + ".conf"):
		print("Group already exists")
		exit(1)

	# Get the server's IP address
	server_ip = get_server_ip(profile_directory, profile)

	# Create the group configuration file
	with open(profile_directory + "/groups/" + name + ".conf", "w") as group_config:
		group_config.write("[Group]\n")
		group_config.write("Name = " + name + "\n")
		group_config.write("Subnet = " + subnet + "\n")
		group_config.write("Profile = " + profile + "\n")
		group_config.write("\n")
		group_config.write("[Server]\n")
		group_config.write("IP = " + server_ip + "/32\n")
		group_config.write("\n")
		group_config.write("[Peers]\n")