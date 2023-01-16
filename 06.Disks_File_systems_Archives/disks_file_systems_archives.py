"""
1. Filesystem Hierarchy Standard (FHS)
Defines the directory structure and directory contents - root level

Directory classification:
- Shareable - User data files and program binaries
- Un-shareable - System-specific information, current installation
- Static - Binaries and scripts
- Variable - user files, mail

/ - Root filesystem, root directory
/boot - Static and un-shareable files related to the booting process
/etc - Static and un-shareable system config files
/bin - Critical executable files
/sbin - Programs usually executed by root
/lib, /lib64 - Program libraries
/usr - Shareable and static
/dev - Hardware devices, files used as interface
/proc - Kernel information as files
/sys - Contains information about devices, drivers, some kernel features
/run - Contains run-time variable data. Exists in memory

2. Archiving tools -  Backup and restore techniques

tar command: sudo dnf install tar
- tar -cvf folder.tar /folder  - Create archive
- tar -xvf folder.tar - Extract from archive

zip command: - Package and compress archive files
- zip file.zip file - Archive of 1 file
- zip -r folder.zip folder - Archive of a folder
- unzip

tar extended:
tar c(t,x) + v + z(gzip) + f(filename)
compressed archive:
tar -czvf archive.tar.gz /etc

3. Disk types:
- Parallel ATA (PATA)
- Serial ATA (SATA) - 7pins, 1 device - 1.5 to 6.0 Gbps /def/sdX
- Small Computer System Interface (SCSI) - 8 or 16 devices /dev/srY

Partitioning and types:
- Primary
- Extended
- Logical
- Special partition Categories

MB vs MiB(mebibyte) - 1000 ** 2, 1024 ** 2
- Master Boot Loader (MBR) - Occupies first 512 Bytes, max size 2 TiB per partition, up to 4 primary partitions
- GUID Partition table - up to 128 partitions, backup, max size 8 ZiB per partition

Linux partition codes:
- Linux filesystem - 83 or 8300
- Linux Swap - 82 or 8200
- Linux LVM - 8e or 8e00

Common partition and filesystem layouts:
    Could be separated:
- /boot - 100 MiB - 1 GiB
- /home - 200 MiB - 3 TiB+
- /opt - 100 MiB - 5GiB
- /var - 100 MiB - 3 TiB+
- /tmp - 100 MiB - 20 GiB

    Should be together:
- /etc, /bin, /sbin, /lib, /lib64, /dev, /usr

Commands:
lsblk - List block devices - lsblk, lsblk -f
fdisk - Manipulate disk partition table
gdisk - GUID partition table
parted - Partition manipulation program
dd - Copy block by block

4. Filesystem Components
- Superblock - Contains the characteristics of the filesystem (size, block size, inode table)
- Inode -  Data structure with system metadata except its name and data
- Data block

- Journal - Keep track of filesystem changes, sudden shutdown

fsck command: Check and repair a Linux filesystem
fsck -V /dev/sdb2

sudo fdisk /dev/sdc - new partition
sudo partprobe command - update partitions
"""