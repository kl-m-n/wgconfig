#!/usr/bin/env python3
import argparse
import utils



def main():
	parser = argparse.ArgumentParser(description="Wireguard Configuration Tool")

	# Create new object
	parser.add_argument("-c", "--create", help="Specify objet type (profile, peer)")
	parser.add_argument("-n", "--name", help="Object name")
	parser.add_argument("-s", "--subnet", help="Subnet (e.g. 192.168.0.0/24)")
	parser.add_argument("-P", "--port", help="Port (e.g. 51820)")
	parser.add_argument("-g", "--group", help="Group name")
	parser.add_argument("-p", "--profile", help="Profile name")
	parser.add_argument("-N", "--networks", help='Allowed networks (e.g. "192.168.0.0/24, 172.16.0.0/16")')
	parser.add_argument("-e", "--endpoint", help="Endpoint (e.g. vpn.example.com:51820)")

	args = parser.parse_args()

	# Create a profile
	if args.create == "profile":
		# Validate arguments
		if not args.name:
			print("You must specify a profile name")
			exit(1)
		if not args.subnet:
			print("You must specify a subnet")
			exit(1)
		if not args.port:
			print("You must specify a port")
			exit(1)
		utils.create_profile(args.name, args.subnet, args.port)

	# Create a group
	if args.create == "group":
		# Validate arguments
		if not args.name:
			print("You must specify a group name")
			exit(1)
		if not args.profile:
			print("You must specify a profile")
			exit(1)
		if not args.subnet:
			print("You must specify a subnet")
			exit(1)
		utils.create_group(args.name, args.profile, args.subnet)	

	# Create a peer
	if args.create == "peer":
		# Validate arguments
		if not args.name:
			print("You must specify a peer name")
			exit(1)
		if not args.networks:
			print("You must specify allowed networks")
			exit(1)
		if not args.endpoint:
			print("You must specify an endpoint")
			exit(1)
		if not args.profile:
			print("You must specify a profile")
			exit(1)
		if not args.group:
			print("You must specify a group")
			exit(1)

		utils.create_peer(args.name, args.networks, args.endpoint, args.profile, args.group)

if __name__ == "__main__":
	main()