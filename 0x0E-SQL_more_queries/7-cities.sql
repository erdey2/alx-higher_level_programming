-- create a table in a given database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states
(
	id INT UNIQUE AUTO_INCREMENT primary key,
	name VARCHAR(256) NOT NULL
);
