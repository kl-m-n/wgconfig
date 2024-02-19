import os
import ipaddress

import utils
from utils import wg_install_path
from utils.get_next_available_ip import get_next_available_ip


def create_peer(name, networks, endpoint, profile, group):
	# Setup directories
	profile_directory = wg_install_path + "/profiles/" + profile
	peer_directory = profile_directory + "/peers"
	profile_configuration = profile_directory + "/" + profile + ".conf"
	peer_configuration = peer_directory + "/" + name + ".conf"
	group_configuration = profile_directory + "/groups/" + group + ".conf"

	# Check if the profile exists
	if not os.path.isdir(profile_directory):
		print("Error: Profile not found")
		exit(1)

	# Check if the peer already exists
	if os.path.isfile(peer_directory + "/" + name + ".conf"):
		print("Error: Peer already exists")
		exit(1)

	# Check if the group exists
	if not os.path.isfile(group_configuration):
		print("Error: Group not found")
		exit(1)

	# Create the peers directory
	if not os.path.isdir(peer_directory):
		os.mkdir(peer_directory)

	# Create keys
	os.system("wg genkey | tee " + peer_directory + "/" + name + ".private | wg pubkey > " + peer_directory + "/" + name + ".public")

	peer_ip = get_next_available_ip(group_configuration)
	if not peer_ip:
		exit(1)

	# Create client configuration file
	with open(peer_configuration, "w") as config:
		config.write("[Interface]\n")
		config.write("PrivateKey = " + open(peer_directory + "/" + name + ".private", "r").read())
		config.write("Address = " + peer_ip + "/32\n")
		config.write("\n")
		config.write("[Peer]\n")
		config.write("PublicKey = " + open(profile_directory + "/" + profile + ".public", "r").read())
		config.write("AllowedIPs = " + networks + "\n")
		config.write("Endpoint = " + endpoint + "\n")
		config.write("\n")

	# Add the peer to the group's configuration file
	with open(group_configuration, "a") as group_config_file:
		group_config_file.write("Name: " + name + "\n")
		group_config_file.write("PublicKey = " + open(peer_directory + "/" + name + ".public", "r").read())
		group_config_file.write("IP = " + peer_ip + "/32\n")
		group_config_file.write("\n")

	# Add the peer to the server's configuration file
	with open(profile_configuration, "a") as server_config_file:
		server_config_file.write("# Name: " + name + "\n")
		server_config_file.write("[Peer]\n")
		server_config_file.write("PublicKey = " + open(peer_directory + "/" + name + ".public", "r").read())
		server_config_file.write("AllowedIPs = " + peer_ip + "/32\n")
		server_config_file.write("\n")