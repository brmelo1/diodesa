#! /bin/bash

echo "Atualizando servidor"

apt update
apt upgrade - y

echo "Instalando Apache 2"

apt install apache2 -y

echo "Instalando Unzip"

apt install unzip -y

cd /tmp
echo "baixando arquivos"
wget https://github.com/denilsonbonatti/linux-site-dio/archive/refs/heads/main.zip
echo "tranferindo arquivos"
unzip main.zip
cd linux-site-dio-main
cp -R * /var/www/html/
echo "Finalizado"



