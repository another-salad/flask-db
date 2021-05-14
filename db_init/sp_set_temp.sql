USE local_db;

DELIMITER $$

CREATE PROCEDURE set_temp(
	IN in_temp VARCHAR(10),
    IN in_error VARCHAR(255)
)

BEGIN
	INSERT INTO temp_data (temp, error) VALUES (in_temp, in_error);
END$$

DELIMITER ;