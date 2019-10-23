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


#create user for wp
echo "creating SQL user"
SQL_PASS=$(randpass)
SQL_USER=admin
CREATE_SQL_USER="CREATE USER '$SQL_USER'@'localhost' IDENTIFIED BY '$SQL_PASS';"
sudo mysql -e "$CREATE_SQL_USER"

echo "creating DB"
sudo mysql -e "CREATE DATABASE pari"
sudo mysql pari < paolo/pari.sql

echo "Database [pari] created, password = $SQL_PASS"