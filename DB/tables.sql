DROP DATABASE IF EXISTS hotel_booking_app;

CREATE DATABASE hotel_booking_app;
USE hotel_booking_app;

CREATE TABLE rooms (
  id INT NOT NULL AUTO_INCREMENT,
  room_nr INT NOT NULL,
  price FLOAT NOT NULL,
  floor INT NOT NULL,
  PRIMARY KEY (id)
);

CREATE INDEX room_nr_idx ON rooms(room_nr);


CREATE TABLE guests (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  telefon VARCHAR(255) NOT NULL,
  room_nr INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (room_nr) REFERENCES rooms(room_nr)
);

ALTER TABLE guests ADD FOREIGN KEY (room_nr) REFERENCES rooms(room_nr);
