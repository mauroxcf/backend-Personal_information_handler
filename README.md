# backend-Personal_information_handler

This repo contains a demostration of a RestFul API with Python using Flask microframework, you can run in your localhost, handle a complete CRUD using Mysql Maria DB.

## Installation
##### Please see the **requirements.txt** file and install the necessary dependencies

The dependencies that we are going to use are Flask, SQLAlchemy, mysqlclient to connect to our database, and the most important, a isolated virtual enviroment.

`check the current version of python on your machine, if it is not installed, you can find the installer on its official page`

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install virtualenv
```bash
Pip install virtualenv
```
them follow the next commands to create the virtual enviroment
```bash
py -m virtualenv venv
```

activate the virtual enviroment in Linux or MacOs
```bash
source venv/bin/activate
```
activate the virtual enviroment in Windows
```bash
.\venv\Scripts\activate
```

install all dependencies
```bash
pip install -r requirements.txt
```

## How to run in localhost :computer:
after complete the installations.
- Create the file .env in the main directory of the app to set our enviroment variables like this:
```python
#set the config of the app run
FLASK_APP=index.py
FLASK_DEBUG=1

# this is the database URI configuration, make all the necessary changes
# is important to have the mysql service running in your machine
MYSQL_USER = here a user
MYSQL_PASSWORD = here the password
#here example of the host, just change the numbers for the ones of your database used
MYSQL_HOST = localhost:3306
MYSQL_DATABASE = here the database
```
and finally
```bash
flask run
```
with all this you flask application should be running in your machine connected to your DB.

## Endpoints :dart:
Here is all the end points that you can use:
​
| HTTP Method | Endpoint | Description |
| ------ | ------ | ------ |
| GET | /api/v1.0/ | Return the status of the API to check that it works. |
| GET | /api/v1.0/all/ | Returns the persons that already registred in the database. |
| POST | /api/v1.0/new/ | Create a new person. |
| POST | /api/v1.0/update/[id] | Match the person id passed, and update the fields of this. |
| GET | /api/v1.0/person/[id] | Match the person id passed, and return his information. |
| GET | /api/v1.0/delete/ | Delete a person. |
​

## How to test
use Postman to test the endpoints, follow the next examples:
- create a person
![image](https://user-images.githubusercontent.com/66022141/188405281-e54ed42d-3bda-43e5-9e8c-af612a546acc.png)
- get all persons
![image](https://user-images.githubusercontent.com/66022141/188405379-d2ad6310-54e2-49a0-be47-ac56e17dba84.png)
- delete a person
![image](https://user-images.githubusercontent.com/66022141/188405451-fea27c5b-ac7e-490f-bc96-070e38c60845.png)
- update a person
![image](https://user-images.githubusercontent.com/66022141/188405515-7d3eaf8e-2ca9-4e2b-9903-4317d8c33576.png)

## Colaborators :busts_in_silhouette:
Mauricio Contreras - [Github](https://github.com/mauroxcf) / [Twitter](https://twitter.com/MauroJCF)  / [Linkedin](https://www.linkedin.com/in/mauricio-contrerasf/)
