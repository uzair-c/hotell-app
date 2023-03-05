# Hotell Application 

### Hotell Application a web application built with Flask, which allows users to manage guests and rooms for an event.

## Installation

To run this app, you will need to have Docker installed on your system. 
Once you have Docker installed, you can build and run the app using the following commands:


## Link
```bash
https://github.com/uzair-c/hotell-app
```

Download the code from Github and cd into location.


## Frontend
```bash
docker build -t frontend .
docker run -d -p 8080:80 frontend
```

## Database
```bash
docker build -t room-service-mysql .
docker run -d -p 3306:3306 --name room-service-mysql room-service-mysql
```

## Backend Services
```bash
docker build -t rooms_service .
docker build -t guests_service .
```

## Run Backend Services
```bash
docker run -p 5001:5001 rooms_service
docker run -p 5002:5002 guests_service
```

These commands will build and run the necessary Docker containers for the app to work.


## Usage

Once the app is running, you can access it by navigating to http://localhost:8080 in your web browser.

You can then use the app to manage guests and rooms for your event.
