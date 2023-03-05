FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=hotel_booking_app
ENV MYSQL_USER=admin
ENV MYSQL_PASSWORD=password

ADD ./tables.sql /docker-entrypoint-initdb.d

EXPOSE 3306
