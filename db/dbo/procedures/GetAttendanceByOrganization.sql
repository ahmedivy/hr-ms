DROP PROCEDURE IF EXISTS GetAttendanceDetails;
GO

CREATE PROCEDURE GetAttendanceDetails
  @OrganizationID INT
AS
BEGIN
  SELECT
    a.atd_id AS AttendanceID,
    a.atd_date AS AttendanceDate,
    COUNT(CASE WHEN ad.atd_id IS NOT NULL THEN 1 END) AS PresentEmployees,
    COUNT(CASE WHEN ad.atd_id IS NULL THEN 1 END) AS AbsentEmployees
  FROM
    dbo.attendance a
    LEFT JOIN
    dbo.attendanceDetails ad ON a.atd_id = ad.atd_id
  WHERE
    a.org_id = @OrganizationID
  GROUP BY
    a.atd_id,
    a.atd_date;
END
