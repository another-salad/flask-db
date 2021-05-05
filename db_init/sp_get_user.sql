USE local_db;

DELIMITER $$

CREATE PROCEDURE get_user(
    IN p_un VARCHAR(255),
    OUT p_pw VARCHAR(255),
    OUT p_salt VARCHAR(255)
)

BEGIN
    SELECT pw_hash, salt INTO p_pw, p_salt FROM users WHERE un = p_un;
END$$

DELIMITER ;