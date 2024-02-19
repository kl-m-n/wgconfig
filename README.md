# wgconfig
Wireguard Configuration Tool

This is a simple CLI-based administration tool to manage Wireguard profiles. It enables:
- group-based peers
- automatic IP assignment
- automatic peer configuration

This tool does NOT:
- automatically manage network interfaces of your host server
- manage firewall configuration

Keep in mind that this tool is a side-project so updates are less frequent.

## Installation
1. Clone repositiry to your server
```
git clone https://github.com/kl-m-n/wgconfig.git /etc/wgconfig
```
2. Make tools accessible via wgconfig command
```
ln -s /etc/wgconfig/main.py /usr/local/bin/wgconfig
```

## Usage examples

Creating a new profile
```
wgconfig --create profile --name vpn-clients --subnet "10.1.0.0/15" --port 51820
```


Creating a new group
```
wgconfig --create group --name admins --profile vpn-clients --subnet "10.1.0.0/24"
```


Creating a new peer (user)
```
wgconfig --create peer --name username --group admins --profile vpn-clients --networks "10.1.1.0/24, 10.1.2.0/24" --endpoint vpn.endpoint.com:51820
```