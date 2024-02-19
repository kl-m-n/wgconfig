import ipaddress

def get_next_available_ip(group_config):
	subnet = None
	taken_ips = set()

	try:
		with open(group_config, "r") as config_file:
			for line in config_file:
				if "IP =" in line or "Address =" in line:
					parts = line.split(" = ")
					if len(parts) == 2:
						ip = parts[1].strip()
						taken_ips.add(ip.split('/')[0])
				if "Subnet =" in line:
					parts = line.split(" = ")
					if len(parts) == 2:
						subnet = parts[1].strip()
					
	except FileNotFoundError:
		print("Error: Configuration file not found")
		exit(1)

	if not subnet:
		print("Error: Subnet not found in the configuration file")
		exit(1)

	ip_network = ipaddress.ip_network(subnet, strict=False)
	for ip_int in range(1, ip_network.num_addresses):
		potential_ip = str(ip_network.network_address + ip_int)
		if potential_ip not in taken_ips:
			return potential_ip

	print("Error: No available IP addresses in the subnet")
	return None
