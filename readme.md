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

## Connection

Download mysql workbench here:

https://www.mysql.com/products/community/

INSTRUCTIONS

How to connect to the database:

1) Launch MySQL Workbench if you haven't already

2) Go to Database >> "Manage Connections"

3) A diaglogue box will then appear, be sure to click the "New Button"

4) Change the field "Connection Name" to "COMP4985".

5) Change the "Connection Method" field to "Standard TCP/IP over SSH"

6) Change the "SSH Hostname" field to "ec2-52-13-226-39.us-west-2.compute.amazonaws.com:22".

7) Change the "SSH Username" field to "ubuntu".

8) Change the "SSH Password" to "d@rcy_Pr0!ject".

9) In the "SSH Key File", you must locate the .ppk file for this
project's server.

10) Change the "MySQL Hostname" to "localhost".

11) Change the "MySQL Server Port" to "3306".

12) Change the "Username" to whatever username you are assigned,
And change the "Password" to whatever password you are given as well.

13) Leave all the remaining fields blank, and click "Test Connection".

14) Your workspace should now be connected to the server's database, so you can now work on it remotely.

How to run an sql file on the database:

If you have mysql workbench, do the following:

1) Go into the COMP4985 MySql connection.

2) Click "File" >> "Open SQL Script"

3) Open the SQL file you want to run.

4) Click "File" >> "Run SQL Script"

5) A dialogue box should appear, just change the field "Default Schema Name"
to whatever Schema you're trying to write to. Then, click "Run" at the bottom
of the box.

6) To see the changes, go into the navigator (it's typically on
the left-hand side) and click the refresh button to the right of the bolded word
"SCHEMAS".

WARNING: NEVER Sign in as root user, it could cause potential problems later on.

