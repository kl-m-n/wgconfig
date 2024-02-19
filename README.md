# wgconfig
Wireguard Configuration Tool

This is a simple CLI-based administration tool to manage Wireguard profiles. It enables:
- group-based peers
- automatic IP assignment
- automatic peer configuration

This tool does NOT:
- automatically manage network interfaces of your host server
- manage firewall configuration

Purpose of this tool is to enable repeatable process of configuring Wireguard which can be further automated.

## Requirements
This program will run on any system that meets the following requirements:
- Python 3.6 or higher
- Wireguard installed


## Installation
1. Clone repositiry to your server
```
git clone https://github.com/kl-m-n/wgconfig.git /etc/wgconfig
```
2. Make tools accessible via wgconfig command
```
ln -s /etc/wgconfig/main.py /usr/local/bin/wgconfig
```
3. Set Wireguard permissions if you haven't already
```
umask 077 /etc/wireguard
```
4. Update config.ini with your Wireguard installation folder
```
vi /etc/wgconfig/config/config.ini
```

## Usage examples

#### Create a new profile
This command will create a new profile structure in: <wireguard_install_folder>/profiles/<profile_name>
```
wgconfig --create profile --name vpn-clients --subnet "10.1.0.0/15" --port 51820
```

#### Create a new group
This command will create a new group configuration in: <wireguard_install_folder>/profiles/<profile_name>/groups/<group_name>.conf
```
wgconfig --create group --name admins --profile vpn-clients --subnet "10.1.0.0/24"
```


#### Create a new peer (user)
This command will create a new peer configuration in: <wireguard_install_folder>/profiles/<profile_name>/peers/<peer_name>.conf, .private, .public
```
wgconfig --create peer --name username --group admins --profile vpn-clients --networks "10.1.1.0/24, 10.1.2.0/24" --endpoint vpn.endpoint.com:51820
```

You can then distribute '<peer_name>.conf' files to clients.