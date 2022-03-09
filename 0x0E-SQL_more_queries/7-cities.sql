-- script that creates the database hbtn_0d_usa and the table cities
-- (in the database hbtn_0d_usa) on your MySQL server
CREATE DATABASE IF NOT EXISTS htbn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id INT PRIMARY KEY UNIQUE NOT NULL AUTO_INCREMENT, state_id INT NOT NULL, FOREIGN KEY(AutorId) REFERENCES states(id), name VARCHAR(256) NOT NULL);
