# Pollination

A voting machine designed by a team of BCIT Computer Systems Technology students within the framework of the Data Communication and Internet working option

This repository contains the source code for the server and database of the Pollination voting machine


## installation

SERVER: django/apache with mod_wsgi

installed according to the instructions for production found at:
https://docs.djangoproject.com/en/3.1/topics/install/#install-python
procedure:

- install apache2.4 https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04
sudo apt install apache 
sudo apt install apache2-dev

apache most likely installs listening to port 22, 80, 443

- install python
sudo apt install python3.9 python3.9-dev python3.9-pip

- install mysqlclient https://pypi.org/project/mysqlclient/
sudo sudo apt-get install python3-dev default-libmysqlclient-dev build-essential

- install mod_wsgi https://modwsgi.readthedocs.io/en/master/user-guides/quick-installation-guide.html
mkdir and cd into folder for downloading
wget https://github.com/GrahamDumpleton/mod_wsgi/archive/4.7.1.tar.gz
tar xvfz 4.7.1.tar.gz
cd into unzipped folder

./configure <- look below
this will look for python and apxs. apxs ins installed with apache2-dev. 
python is not always invoqued the same so you may have to point it to python
if either python or apxs are not found you can use
./configure --with-apxs=/usr/local/apache/bin/apxs --with-python=/usr/local/bin/python

make
make install
sudo systemctl restart apache2
make clean
possibly:
cd into apache2 install folder
sudo nano apache2.conf
write LoadModule wsgi_module modules-available/mod_wsgi.so

- install django https://modwsgi.readthedocs.io/en/master/user-guides/quick-installation-guide.html
python -m pip install Django
you may have to replace python with python3.9 or so
this installation completely ignored creating a python virtual environment as there were errors generated 
by the stated procedure



