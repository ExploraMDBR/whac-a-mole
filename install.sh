#!/bin/bash

set eux

function randpass()
{
    local  myresult=$(< /dev/urandom tr -dc '_A-Z-a-z-0-9' | head -c${1:-32};echo;)
    echo "$myresult"
}

sudo apt update

sudo apt install -y mysql-server
read -n1 -p "About to perform mysql conf. User supervision required. press a key to continue."
sudo mysql_secure_installation

#create DB
echo "creating SQL user"
SQL_PASS=$(randpass)
SQL_USER=admin
CREATE_SQL_USER="CREATE USER '$SQL_USER'@'localhost' IDENTIFIED BY '$SQL_PASS';"
sudo mysql -e "$CREATE_SQL_USER"

echo "creating DB"
sudo mysql -e "CREATE DATABASE 	"
sudo mysql pari < paolo/pari.sql

echo "grant admin user permissions"
GRANT_WP_PERMISSIONS="GRANT ALL PRIVILEGES ON pari.* TO '$SQL_USER'@'localhost';"
sudo mysql -e "$GRANT_WP_PERMISSIONS"

#install python3 MySQLdb
sudo apt-get install python3-mysqldb

#init server as deamon
sed -e "s:%WORK_DIR%:$(pwd):g" pari_server.service | sudo tee /etc/systemd/system/pari_server.service  
sudo systemctl enable pari_server.service
sudo service pari_server start

#kiosk
sed -e "s:%WORK_DIR%:$(pwd):g" kiosk.service | sudo tee /etc/systemd/system/kiosk.service 
sudo systemctl enable kiosk.service

#end
echo installation finished
echo "Database [pari] created, password = $SQL_PASS"
echo "Be sure to copy it and paste it in 'database_manager.py'"
echo "Upon restart the system will open Chromium in KIOSK mode"