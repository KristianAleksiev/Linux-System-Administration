"""
1. Environment and env variables - Set up both on system level and user level
General purpose special variables:
$? - Return the exit code of last executed command
$! - Return the PID of the last job run in background
$$ - Return the PID of the current process
$_ - Return the final argument of the previous command

Prompt related special variables:
$PS1 - Regular prompt
$PS2 - Prompt during multi-line commands

"set" command - Controls shell options. Display values of shell variables
"unset" command - Unset values and attrs of shell variables and functions

Command execution => shell => fork() => shell copy => exec(command) - Executed in another shell session,
could be modified and modeled

Sourcing vs Execution - With sourcing the copy of shell isn't executed, the script is directly executed on main shell
. script_address or source script_address - > Sourcing - Execution in main shell
exec script_address -> Execution in subshell

command execution by shell:
- Checks if the command is an Alias, Function, Built-in, Hash, PATH variable. If found executed else command not found.

whereis, which, type (shows command info), alias, unalias  commands

2. Configuration files - BASH shell
System configuration files:
- Stored in /etc
Files:
profile - Used for environment control and startup programs exec
bashrc(centOS) or bash.bashrc(openSUSE, Ubuntu) - Used for Functions and Alias definition
folder profile.d/ - Used for custom routines definition, it is read by profile and bashrc

User configuration files:
- Stored in user's home directory
.bash_profile or .profile - Executed in login shell
.bashrc - Executed always

Depending on the shell sequence different files are read
Environmental changes are put in specific files regarding their purpose,
if user env is changed, the user profile config file is changed -folder etc/profile.d/
if env is changed for all users, the change is applied in system level config files etc.

Checking the environment commands:
alias
set
set +o / -o - params of shell
set -x / +x
MYVAR=Demo
echo MYVAR
export Variable2 - > Inheritance in child process
Child-bash -> env MYVAR2=Child PS1="CHILD:$PS1" bash

Creating an alias (uname):
alias inf="uname -a"
type inf
hash - register for commands, files executed

2. Help resources
- Locally installed
- External

help type
--help, -h, -?
man command (Category 1, 5, 8)
man (SECTION) filename - man 5 passwd
apropos (man -k)

3. Working with files
- Regular files - Regulars, Directories
- Special files - Symbolic links, Block device, Character device, Named pipe, Socket

file X - type of the file
cp file1.txt ~/Documents/my-file.txt - copy a file and save to path
mv file1.txt file2.txt - Renaming a file and moving
rm - delete file
rmdir - delete empty directory
ln - make links between file (hard / soft link), hard links should be on one device

mkdir -pv demo/demo-2/demo-3
mkdir -p dir-{1..10}/subdirectory-{A, B, C}
touch file-{1..5}-{A,B}
ls -l file*
rm -v file*
rm -rv dir-10
ls file?.txt

cp /etc/services . -> Copy the specific file to the relative position
cp -v /etc/services services-copy -> Copy the file and paste it to the relative position with specific name
cp -v services services_local_copy
mv -v services original_services -> Rename the services file to original_services
ls -li
ln services-copy services_link -> 2 objects to same memory space, hard link, only the specific one is deleted
ln -s /etc/services linked-services -> Size is a lot smaller, reference (shortcut)
ln -s original-services services-link

Soft link or Hard link - Depending on the number of file systems

4. Users and groups
/etc/passwd - Users file
username:pw:user_id:user_group:comment:user_home_dir:user_shell

/etc/shadow - Passwords file
username:Encrypted pass:last_pw_change:min_days_between_change:days_validity:expiration_warning:inactivity_expiration_days

Default User creation:
/etc/login.defs
/etc/default/useradd

Default User home files:
/etc/skel/

Groups:
/etc/group
group_name:password_placeholder:group_members_id

User commands:
useradd
usermod
userdel
users - logged users atm
last
lastb
passwd
chpasswd

Group commands:
groupadd
groupmod
groupdel
groups
gpasswd *
sudo - root / another user
"""