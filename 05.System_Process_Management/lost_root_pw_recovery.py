"""
Redhat 9.x => Rescue => linux ($root) line -> rd.break -> Ctrl X enter
mount -o remount,rw /sysroot
chroot /sysroot
passwd
touch /.autorelabel
exit
exit

Debian -> linux line -> rw quiet init=/bin/bash -> Ctrl X
passwd
sudo reboot
"""