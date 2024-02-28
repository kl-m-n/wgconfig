#!/usr/bin/env python3
import argparse
import utils



def main():
	parser = argparse.ArgumentParser(
		description="Wireguard Configuration Tool",
		epilog='For more information, visit github at https://github.com/kl-m-n/wgconfig.',
    	usage='%(prog)s [options]'
	)

	# Create new object
	parser.add_argument("-c", "--create", help="Specify objet type to one of available choices.", choices=["profile", "peer", "group"])
	parser.add_argument("-n", "--name", help="Name your object. Use dash or underscrore instead of spaces")
	parser.add_argument("-s", "--subnet", help='Provide a valid subnet closed in brackets (eg. "192.168.0.0/24").')
	parser.add_argument("-P", "--port", help="Port (e.g. 51820)", type=int)
	parser.add_argument("-g", "--group", help="Name your group. Use dash or underscrore instead of spaces.")
	parser.add_argument("-p", "--profile", help="Name your profile. Use dash or underscrore instead of spaces.")
	parser.add_argument("-N", "--networks", help='Specify allowed networks to pass through VPN (e.g. "192.168.0.0/24, 172.16.0.0/16").')
	parser.add_argument("-e", "--endpoint", help="Specify VPN endpoint (e.g. vpn.example.com:51820).")
	parser.add_argument("-d", "--dns", help="Specify DNS servers (e.g. 1.1.1.1).")

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
		if not args.dns:
			print("You must specify a DNS server")
			exit(1)

		utils.create_peer(args.name, args.networks, args.endpoint, args.profile, args.group, args.dns)

if __name__ == "__main__":
	main()