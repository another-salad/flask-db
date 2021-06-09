USE local_db;

DELIMITER $$

CREATE PROCEDURE get_temp(
    IN num_rows INT
)

BEGIN
	SELECT temp, error, loc, update_date FROM temp_data ORDER BY update_date DESC LIMIT num_rows;
END$$

DELIMITER ;