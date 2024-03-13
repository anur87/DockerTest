CREATE USER anvar with password '123456';

CREATE DATABASE my_database with owner anvar;
grant ALL PRIVILEGES ON DATABASE my_database to anvar;