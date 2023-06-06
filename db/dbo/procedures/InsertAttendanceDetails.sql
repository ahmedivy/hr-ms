CREATE PROCEDURE InsertAttendanceDetails
  @atd_id INT,
  @emp_id INT,
  @time_in TIME,
  @time_out TIME
AS
BEGIN
  INSERT INTO attendanceDetails
    (atd_id, emp_id, time_in, time_out)
  VALUES
    (@atd_id, @emp_id, @time_in, @time_out);
END;
