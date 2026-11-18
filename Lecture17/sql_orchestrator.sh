#!/bin/bash

cd /home/s1306053/BPSM/exercises/Lecture17 || exit

source playtime/bin/activate

read -s -p "MySQL password: " MySQL_password
echo
export MySQL_password

cat ./sql_setup.py
python ./sql_setup.py

cat ./sql_q1_4.py
python ./sql_q1-4.py

unset MySQL_password

deactivate



