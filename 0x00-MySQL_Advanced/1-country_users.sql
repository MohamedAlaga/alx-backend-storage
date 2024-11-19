--  SQL script that creates a table users
create table
    if not exists users (
        id int unique not null AUTO_INCREMENT,
        email varchar(255) not null unique,
        name varchar(255),
        country enum ('US', 'CO', 'TN') default 'US' not null
    );