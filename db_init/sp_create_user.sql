USE local_db;

DELIMITER $$

CREATE PROCEDURE create_user(
	IN p_un VARCHAR(255),
    IN p_pw VARCHAR(255),
    IN p_salt VARCHAR(255)
)

BEGIN
	INSERT INTO users (un, pw, salt) VALUES (p_un, p_pw, p_salt);
END$$

DELIMITER ;