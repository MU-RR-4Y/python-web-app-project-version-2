DROP TABLE IF EXISTS wishlists;
DROP TABLE IF EXISTS visits;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS destinations;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    climate VARCHAR(255),
    currency VARCHAR(255)
    
);

CREATE TABLE destinations(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    information VARCHAR(255),
    country_id INT NOT NULL REFERENCES countries(id) ON DELETE CASCADE
 );
 


CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE visits(
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    destination_id  INT REFERENCES destinations(id) ON DELETE CASCADE,
    date VARCHAR(225),
    rating INT,
    comment VARCHAR(255)

);

CREATE TABLE wishlists(
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    destination_id INT REFERENCES destinations(id) ON DELETE CASCADE
)

