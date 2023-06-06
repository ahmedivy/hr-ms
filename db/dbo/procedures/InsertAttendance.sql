CREATE PROCEDURE InsertAttendance
    @att_date DATE,
    @org_id INT
AS
BEGIN
    INSERT INTO attendance (atd_date, org_id)
    VALUES (@att_date, @org_id);

    SELECT * FROM attendance
    WHERE atd_id = SCOPE_IDENTITY();
END;


EXEC InsertAttendance '2019-01-01', 106;
EXEC InsertAttendance '2019-01-01', 107;

SELECT * FROM attendance;

