# Pollination

A voting system created by BCIT Datacomm students

## Members:
- Karel Chanivecky - Team Lead/Server

## Installation

### Linux - Ubuntu 20.04

#### Install Nginx

    sudo apt install nginx
1. Create /var/www/
1. Navigate to /var/www/
1. Clone our data-base server repo
1. Navigate to /etc/nginx/sites-available
1. Create a new file named after your domain <my_domain.ca>
1. Ensure contents of file are as such:
1. Create a hardlink of file to /etc/nginx/sites-enabled
    At the given folder:
        sudo ln <my_domain.ca> ../sites-enabled
1. Start nginx
    sudo service start nginx
1. Ensure that your page is available. Note that at this point it will only be available with HTTP
1. Install and run certbot by following the instructions here:
    https://certbot.eff.org/instructions
    
    Warning!! Do not do this step before your page is working
1. Verify that HTTPS is working

1. Go to the server folder and run it
    sudo python -m swagger_server

#### Install Database

1. Install MySQL
1. Deploy the schema found in ... by doing ... 

#### Install depedencies
1. Install python3.9
1. Install mysqlclient
    

    sudo apt-get install python3-dev default-libmysqlclient-dev build-essential

    sudo apt install python-dev python3-dev python3.9-dev

    pip install mysqlclient

1. Go to server root directory and enter
   
    pip install -r requirements.txt

1. Create file ~/.my.cnf
    
    Type: 
   
        [client]
        user=root
        password="pass"
        
        [mysql]
        user=root
        password="pass"
        
        [mysqldump]
        user=root
        password="pass"
        
        [mysqldiff]
        user=root
        password="pass"
    
    
   