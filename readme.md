# Pollination

A voting machine designed by a team of BCIT Computer Systems Technology students within the framework of the Data Communication and Internet working option

This repository contains the source code for the server and database of the Pollination voting machine

--------------------------------------------

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

12) Change the "Username" to "root".

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