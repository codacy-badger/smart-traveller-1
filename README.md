# Smart Traveller
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8959f68ace3d46aab39f394abdd2fd72)](https://www.codacy.com/manual/anyric/smart-traveller?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=anyric/smart-traveller&amp;utm_campaign=Badge_Grade)
## Description
Smart Traveller is a Django Restful API for managing bus booking and ticketing operations in a more convinient, efficient and effective manner for both passengers and bus operators.

## Table of Contents
- [Key Features](#key-features)
- [Setup](#setup)
    - [Dependencies](#dependencies)
    - [Getting Started](#getting-started)
- [Running the application](#running-the-application)
- [Testing](#testing)
- [Docker Environment](#docker-environment)

## Key Features
    1. User Management
    2. Agent Management
    3. Fleet Management 
    4. Trip Management
    5. Ticket Management

## Setup
### Dependencies
* [Python 3.8](https://www.python.org/) - popular general-purpose scripting language suited for web development
* [Django 3.0](https://docs.djangoproject.com/en/3.0/) - A web application framework for Python
* [Djangorestframework 3.11](https://www.django-rest-framework.org/) - A powerful and flexible toolkit for building Web APIs

### Getting Started
Setting up project in development environment
* Ensure Python 3.8 is installed by running:
```
python --version
```
* Ensure pipenv is installed or you can follow the intallation from [PIPENV](https://docs.pipenv.org/)
* Create a folder for the project by running:
```
mkdir myprojectfoldername
```
* cd in to `myprojectfoldername`
* Create a virtualenv using pipenv by running:
```
pipenv shell
```
* Clone the project repo by running:
```
git clone https://github.com/anyric/smart-traveller.git
```

### Database setup
Create a database locally on your machine named `smarttravel` and add the name as a value to the environment variable. Use the `env.sample` template to create a .env file

### Running the application
* Export the .env file by running 
```
. .env
```
* Inside the project root folder i.e smarttravellersapi/, run the command below in your console
```
python manage.py migrate

python manage.py runserver
```
* Using Postman, create a new account by navigating to `http://127.0.0.1:8000/api/v1/users/` with request body format like this
```
{
	"username":"",
	"mobile":"",
	"email":"",
	"first_name":"",
	"last_name":"",
	"password":""
}
```
* Login to generate a token at `http://127.0.0.1:8000/api/v1/auth/login/` with request body format like this
```
{
	"username":"",
	"email":"",
	"password":""
}
```
* Use the token to interact with other CRUD endpoints.

### Testing
* Export the .env file as describe above if you haven't 
* Run the command below:
```
python manage.py test
```

### Docker Environment
#### Running a Docker development Environment
#### Prerequisites
 - docker
 - docker-compose

#### Setup local docker development environment
* Clone the repository and navigate to the root folder.

#### To build docker images
Run the command below:
```
make build
```

#### To start the local development server
Run the command below:
```
make start
```

#### Running tests
Run the command below:
```
make test
```

#### Stoping the development server
```
make stop
```

#### Cleaning up local docker environment
```
make clean
```

## Developer and Maintainer
* Anyama Richard
