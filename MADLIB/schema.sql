DROP TABLE if exists users;
CREATE TABLE users (
    id integer PRIMARY KEY autoincrement,
    business_name 	text NOT NULL,
    business_type 	text NOT NULL,
    market_type     text NOT NULL,
    job_to_be_done 	text NOT NULL,
    revenue_model 	text NOT NULL

);
