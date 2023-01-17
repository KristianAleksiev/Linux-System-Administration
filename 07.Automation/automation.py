"""
1. Scheduled task execution
Main task scheduler in LX - cron
crond - Service
crontab - Management tool

Config files:
Tasks are read from /etc/crontab and /etc/cron.d/
Rights are read from /etc/cron.allow and /etc/cron.deny

Execution template:
minute hour month_day month week_day path_to_executable
* * * * * /utilities/backup.sh - Execute every minute
0 12 * * * /utilities/backup.sh - Execute every noon at 12:00
0 */2 * * * /utilities/backup.sh - Execute every two hours daily
0 9-17 * * * /utilities/backup.sh - Execute every hour between 9 and 17 every day

Cron shortcuts:
@yearly (@annually)
@monthly
@weekly
@daily
@midnight
@hourly

anacron - Runs commands periodically with frequency in days
It does not assume that the machine is non-stop powered, executes when the machine turns on

at - Runs a task once at a specific time - NOW + N hours
atq - queue of tasks to execute,
atrm - delete all tasks

systemd timer

Cases At:

systemctl status atd
sudo systemctl enable --now atd
at 20:20
echo $(date) >> /tmp/at1.log
Ctrl + D

at now + 2 minutes
echo $(date) >> /tmp/at2.log

at now + 30 minutes
tar czvf /tmp/etc.tar.gz /etc 2> /tmp/at3.log

atrm 3 - Remove task 3
atq

Cases crond:
systemctl status crond
crontab -e
* * * * * wall "Scheduled task run success"
crontab -l -> check for the defined task

crontab -e
*/3 * * * * ps ax | wc -l >> /tmp/running_processes.log


tar -czf test.tar.gz /etc > /tmp/tar.log 2>&1
date +\%Y-\%m-\%d
tar -czf test-$(date +\%Y-\%m-\%d).tar.gz /etc > /tmp/tar.log 2>&1
"""