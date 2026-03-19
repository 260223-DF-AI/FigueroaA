CREATE DATABASE training_db;

CREATE TABLE associates(
    associate_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    hire_date DATE DEFAULT CURRENT_DATE
)

INSERT INTO associates 
(first_name, last_name, email)
VALUES 
('Dylan', 'Parrot', 'dylan.parrot@revature.net'),
('Lee', 'Wilson', 'lee.wilson@revature.net');

INSERT INTO associates
(first_name, last_name, email, hire_date)
VALUES
('Alec', 'Figueroa', 'alec.figueroa@revature.net', '2026-02-20')

SELECT * FROM associates
