#!/bin/bash
echo "Starting *sh commands"
cd /home
current_date_time=`date +"%Y-%m-%d %T"`
git pull https://github.com/KateSharkun/Todo.git
git commit -m 'deploy on $current_date_time'
git push
systemctl restart todo
systemctl status todo
