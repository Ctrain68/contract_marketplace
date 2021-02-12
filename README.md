


## Installation

### Dependancies


Create a new directory and cd into it
* Clone git repo
* If not running python 3.8, run the following bash commands

* sudo apt update
* sudo apt install python3.8
* Create a virtual enviornment
* sudo apt-get install python3-pip
* sudo apt-get install python3-venv
* python3 -m venv venv
* source venv/bin/activate
* Install the modules in requirements.txt
* cd into folder
* pip install -r requirements.txt
* Run the Program
* cd src
* set flask variables
* ```$ export FLASK_APP=main.py.py```
* ```   $ export FLASK_ENV=development```
*```flask run```


A Swagger file is also available showing the endpoints. A database has been deployed on an EC2 instance and is synced to the .env file in this project. To perform all duties relation to admin please login as:
 * email:test0@test.com 
 * password: 123456 

 You shall need to copy the JWT token generated to perform actions required. This particular user is the only one with admin rights which is restricted in the database dump end point.
 The endpoint "/equipment/" contains the html representation of some of the output from this application.

 The database has been seeded with faker and random generated data. There is a copy of the migrations for the database in migrations/versions.


## Produces a professional report that provides an analysis of privacy and security concerns relating to a system

