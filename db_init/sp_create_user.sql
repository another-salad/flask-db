USE local_db;

DELIMITER $$

CREATE PROCEDURE create_user(
	IN p_un VARCHAR(255),
    IN p_pw VARCHAR(255)
)

BEGIN
	INSERT INTO users (un, pw_hash) VALUES (p_un, p_pw);
END$$

DELIMITER ;