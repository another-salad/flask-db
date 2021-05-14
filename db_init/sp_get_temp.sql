USE local_db;

DELIMITER $$

CREATE PROCEDURE get_temp(
    IN num_rows INT
)

BEGIN
	SELECT temp, error, update_date FROM temp_data LIMIT num_rows;
END$$

DELIMITER ;