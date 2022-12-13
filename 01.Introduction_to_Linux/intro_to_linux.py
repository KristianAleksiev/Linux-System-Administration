"""
1. Introduction to Linux

Kernel - Core of the OS, manages the hardware
Process - Program that the kernel manages
Kernel space - Area of memory that only the kernel can access
User space - Memory allocated by the kernel for user processes
Users:
- Owner of files and can run processes, has permissions and boundaries
- Superuser (root), system users, regular users
- Users in a group share file access

1.1. Linux system architecture
Hardware - CPU, RAM, HDD, NET
Linux kernel - System calls/funcs, Memory management, Process management, Device drivers
User processes - GUI, Shell, Services

1.2. Linux Ecosystem and Distro families
Linux Distribution:
- System components:
Boot Loader
Boot Manager
Kernel

- User components
Daemons
Shell
Graphical Environment
User Applications

Family criteria:
- Same code base
- Same package management system
- Members are derivatives
- Specific usage of the distro of the same family (different purpose)
- Documentation and Support

Distro families:
- Debian (Ubuntu, Kali),  Ubuntu Server 22.04 (Debian 11)
- Fedora (RedHat) - Redhat linux, Oracle linux, AlmaLinux OS 9.0
- openSUSE - Gecko, SUSE Linux distribution, openSUSELeap 15.4
- Arch

- Certifications
LPI, Linux Foundation

2. Virtualization and installation of a Linux distro
- VirtualBox introduction - Hypervisor or Virtual machine monitor
Type 1 (servers), Type 2 (hosted hypervisor)
Import / Export machine

3. First steps in the console
Environmental variables
echo $SHELL - Display the variable's value
printenv - List environment variables
cat - Print the contents of the file
cal - Display a calendar
hostname
hostnamectl
uname - Distro info
uptime - How log the system is running
history - Command history list
exit
wall - Send message to everybody's terminal
systemctl status sshd - Check if we have ssh service

Connection Options:
- Local - VM Console connection
- Remote - SSH Client(host) SSH service(guest) - Requires network connection

ssh client - PuTTY

"""