CREATE DATABASE mc_server_log;
use mc_server_log;

CREATE TABLE default_server_user_log (
    id int NOT NULL AUTO_INCREMENT,
    users VARCHAR(300),
    date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

INSERT INTO default_server_user_log
    (users)
VALUES
    ('test_user_1, test_user_2');
