use local_db;

CREATE TABLE default_server_active_user_log (
    id int NOT NULL AUTO_INCREMENT,
    active_users VARCHAR(255),
    server_name VARCHAR(100),
    date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

INSERT INTO default_server_active_user_log
    (active_users, server_name)
VALUES
    ('test_user_1, test_user_2', 'test_server');
