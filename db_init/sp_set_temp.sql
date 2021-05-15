USE local_db;

DELIMITER $$

CREATE PROCEDURE set_temp(
	IN in_temp FLOAT,
    IN in_error BOOLEAN,
	IN in_loc VARCHAR(255)
)

BEGIN
	INSERT INTO temp_data (temp, error, loc) VALUES (in_temp, in_error, in_loc);
END$$

DELIMITER ;