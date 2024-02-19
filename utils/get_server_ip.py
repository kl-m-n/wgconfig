import ipaddress

def get_server_ip(directory, name):
	try:
		with open(f"{directory}/{name}.conf", "r") as server_config_file:
			for line in server_config_file:
				if "Address" in line:
					return line.split("Address = ")[1].split('/')[0].strip()
				
	except FileNotFoundError:
		print("Error: Configuration file not found")
		exit(1)