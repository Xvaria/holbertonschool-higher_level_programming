-- Read user
-- Creates the database hbtn_0d_2, If the database already exists, script not fail
-- Creates the user user_0d_2, If the user already exists, script not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON * . * TO 'user_0d_2'@'localhost';
