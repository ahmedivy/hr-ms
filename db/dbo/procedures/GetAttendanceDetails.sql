DROP PROCEDURE IF EXISTS GetAttendanceDetails;
GO

CREATE PROCEDURE GetAttendanceDetails
  @OrganizationID INT
AS
BEGIN
  DECLARE @TotalEmployees INT;

  SELECT @TotalEmployees = COUNT(*)
  FROM dbo.employees
  WHERE org_id = @OrganizationID;

  SELECT
    a.atd_id AS AttendanceID,
    a.atd_date AS AttendanceDate,
    COUNT(CASE WHEN ad.atd_id IS NOT NULL THEN 1 END) AS PresentEmployees,
    @TotalEmployees - COUNT(CASE WHEN ad.atd_id IS NOT NULL THEN 1 END) AS AbsentEmployees
  FROM
    dbo.attendance a
    INNER JOIN
    dbo.attendanceDetails ad ON a.atd_id = ad.atd_id
  WHERE
    a.org_id = @OrganizationID
  GROUP BY
    a.atd_id,
    a.atd_date
  ORDER BY
    a.atd_date DESC;
END


SELECT *
FROM [dbo].[Attendance]

SELECT *
FROM [dbo].[AttendanceDetails]

SELECT *
FROM [dbo].[AttendanceDetails]
  LEFT JOIN [dbo].[Attendance] ON [dbo].[AttendanceDetails].[atd_id] = [dbo].[Attendance].[atd_id]

EXEC GetAttendanceDetails 106