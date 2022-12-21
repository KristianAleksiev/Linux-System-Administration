"""
1. Network and services
-OSI Models Layers:
Physical
Data-Link
Network
Transport
Session
Presentation
Application

-TCP/IP Protocol Architecture Layers
IP - Internet Protocol - Handles addressing and communication between devices
TCP - Transmission Control Protocol - Complements IP and focuses on the transport of data packages
UDP - User Datagram Protocol - Like TCP but without connection
ICMP - Internet Control Message Protocol - Networking devices (routers) are  using it

Port Numbers: Used to identify a network service => /etc/services -
Types of ports -> Well-known(system ports) - 0 - 1023, Registered (user) - 1024 - 49151, Dynamic(private)- 49152 - 65535
22-SSH, 53-DNS, 80-HTTP, 110-POP3, 123-NTP, 143-IMAP

IP Address: Static (Being inputted) or dynamic(Get from somewhere)
Network mask - subnet mask - > The border between two networks (border of network)
Gateway address - Connection between two networks (which are not in the same network)
Broadcast address - Communication to all hosts on a network
IP Protocol versions - IPv4(4 bytes, 32 bits), IPv6(6 bytes, 48 bits),
binary or decimal format (0.0.0.0, 255.255.255.255) - Divided in two part - Network and host

Network interface
Internet
Host-to-Host Transport
Application

-Protocols
TCP:
-- Telnet
-- FTP
-- SMTP

UDP:
-- DNS
-- RIP
-- SNMP

Config management:
Network manager(RedHat, Debian), SystemD network(RedHat, Debian), Wicked (OpenSUSE)

systemctl start sshd.service
systemctl stop sshd.service
systemctl reload sshd.service
systemctl restart sshd.service
systemctl status sshd.service
systemctl show sshd.service
systemctl enable sshd.service
systemctl disable sshd.service
As root

ip link show (ip l)
sudo ip link set dev enp0s8 down
ip address show
sudo ip address add 192.168.200.1/24 dev enp0s8 - Add ip address to a card - Runtime config
ping 192.168.200.1

# Redhat distros
nmcli general status
nmcli connection show
sudo nmcli connection del "Wired connection 1"
sudo nmcli connection add type ethernet ifname enp0s8 con-name static-internal
sudo nmcli connection modify static-internal ipv4.addresses 192.168.200.1/24 ipv4.method manual

2. Software Management
- Static vs dynamic libraries linking - rpm / deb
rpm - works with  local packages
rpm command:
rpm -qa
rpm -q kernel
rpm -qc openssh

YUM / DNF
/etc/yum.conf

yum list
yum list httpd
yum list http*
yum search ...
yum groups install "GNOME Desktop"
yum groups erase "GNOME Desktop"
yum install epel-release
yum r epolist

Alma:
sudo dnf upgrade
dnf search wget
dnf repolist (--all)
sudo dnf install -y epel-release
dnf group list
dnf module list

3. Basic Network services
- Firewall - firewalld - Dynamically managed firewall with support for zones, managed through cmd interface - firewall-cmd

sudo firewall-cmd --state
firewall-cmd --get-zones
firewall-cmd --get-default-zone
sudo firewall-cmd --set-default-zone=internal
firewall-cmd --get-services
sudo firewall-cmd --add-service=http --permanent (or runtime)
sudo firewall-cmd --add-port=22/tcp --permanent
sudo firewall-cmd --reload - Reload the firewall configuration

FTP - File transfer protocol - File transfer between a client and a server systems - port 21

sudo dnf install -y dhcp-server - main host
sudo vi /etc/dhcp/dhcpd.conf - setting up the ip addresses, global settings, local settings for each host
sudo dhcpd -t - test the configuration
sudo systemctl start dhcpd - start the service
sudo systemctl enable dhcpd - permission, when server is restarted, the service runs automatically
systemctl status dhcpd - status of the service

On different hosts:
ip a
sudo nmtui - activate
cat /etc/resolv.conf
ip r - default root

On main => Leases file
cat /var/lib/dhcpd/dhcpd.leases, DIFFERENT MACs

PACKET FORWARDING ON GATEWAY: (Main)
systemctl status firewalld
firewall-cmd --get-active-zones
sudo nmcli connection modify enp0s3 connection.zone external
sudo nmcli connection modify static-internal connection.zone internal
firewall-cmd --get-active-zones

cat /proc/sys/net/ipv4/ip_forward => nameserver 8.8.8.8

"""