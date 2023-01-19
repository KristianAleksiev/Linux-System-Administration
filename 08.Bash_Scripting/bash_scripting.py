"""
1. Bash scripting building blocks
Scripts. Structure and variables
- Script signature - Tells the system which interpreter to use (path)
- Comments
- Local variable
- Command

Bash scripting commands:
- echo ''
- printf '' - printf '%d' X - placeholder
- seq - seq 1 3 - 1 2 3 -
- for i in $( ls ); do echo item: $i done, C style for loop also available

2. Writing scripts in bash
Script case:
vi script1.sh
bash script1.sh

chmod +x script1.sh
/home/user/script1.sh

#!/bin/bash
#Create a user
username=test
echo "* Create user $username"
useradd -m -s /bin/bash $username
echo "* Set password for the $username user"
passwd $username
echo "* Create a readme.txt file"
echo "Welcome, $username" > /home/$username/readme.txt
echo "* Done."

#!/bin/bash
#sourcing vs execution
echo "MYVAR=$MYVAR"
echo "Executed on $(date)" | tee /tmp/s4.txt

#!/bin/bash
#Sourcing vs Execution
MYVAR=Hello
echo "MYVAR=$MYVAR"
echo "Executed on $(date)" | tee /tmp/s4.txt
    source script.sh (child bash, current session)

Special variables:
$0, $1.. ${10}, $# - number of parameters
if [$3 -ne 1]; then ...... exit 1 (break); fi

Interactive prompt for user input:
read -p "Enter input here: " USR_NAME
echo 'Hello, ' $USR_NAME



"""