CREATE PROCEDURE [dbo].[GetAttendanceDetailByID]
  @atd_id int
AS
BEGIN
  SELECT
    e.emp_id,
    e.emp_firstname + ' ' + e.emp_lastname AS emp_name,
    ad.time_in,
    ad.time_out,
    DATEDIFF(HOUR, ad.time_in, ad.time_out) AS work_hours
  FROM
    [dbo].[AttendanceDetails] ad
    INNER JOIN [dbo].[employees] e ON ad.[emp_id] = e.[emp_id]
  WHERE ad.[atd_id] = @atd_id
END
