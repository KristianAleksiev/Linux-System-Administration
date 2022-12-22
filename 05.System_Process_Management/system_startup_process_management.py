"""
1. System startup and Boot managers
BIOS systems:
Power on -> BIOS (POST - Checking hardware and configuration, Looking for first sector in the HDD, Transfer of control) ->
MBR (Stage 1 Boot loader, 1.5) -> Boot loader(Stage 2, os loading) ->

UEFI systems:
Power on -> UEFI (POST) --> EFI Boot loader (ESP partition)

Boot Loaders:
LILO (very old, rare)

GRUB/GRUB2 ( GNU grand unified boot loader) - Customizable, own shell, /etc/grub (default/grub
grub(2)-mkconfig, Boot loader and boot manager together
After GRUB2 -> Kernel(Check hardware again, to be prepared for usage(drivers, settings etc), INITRD(helps kernel, unload) ->
System INIT Process (Prompts, cards configs, user configs, Sys5init, systemd) -> User programs

SYSLINUX (Live media)
Loadlin (Booting from non-Linux OS)

2. systemd Components
systemd - system ans services manager
systemctl - state inspection and state controlling utility
systemd-analyze - utility for performance statistics inspection
journald - logging component by default
consoled - consol daemon
networkd - network support
logind - display managers

Commands:
dmesg -H - Kernel ring buffer (RAM Area)
efibootmgr (uefi) - Manipulate the EFI Boot manager through OS
dmesg | grep -i vga / usb

systemd Units: (Init scripts) system, target unit
Naming convention for units - "unit name"."unit type" - /usr/lib/systemd/system
systemctl get-default
systemctl list-units --type=target
systemctl status sshd
journalctl --reverse _SYSTEMD_UNIT=sshd.service
systemd-analyze time
systemd-analyze critical-chain

3. Processes and Resources
- Processes Monitoring and Management
Process, Job (Suspended, program that doesn't detach, it can execute in foreground or background)
Jobs commands:
jobs
fg
bg - background
ps - processes
pstree - tree of processes
kill - signal to kill a process,
killall - signal to a group of processes
Process priorities: Priority level to the CPU time

- Resource monitoring
Commands:
free - free and used memory in system
df - free disk space
du - disk space usage
vmstat - virtual memory statistics
ps
ps lf

"""