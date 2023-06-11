
CREATE PROCEDURE GetMonthlySalarySheet
    @org_id INT,
    @month INT,
    @year INT
AS
BEGIN
    SELECT
        e.emp_id,
        CONCAT(e.emp_firstname, ' ', e.emp_lastname) AS 'Employee',
        e.emp_hourly_rate,
        SUM(DATEDIFF(HOUR, ad.time_in, ad.time_out)) AS 'Total Hours',
        SUM(DATEDIFF(HOUR, ad.time_in, ad.time_out)) * e.emp_hourly_rate AS 'Total Pay'
    FROM
        [dbo].[attendanceDetails] ad
    INNER JOIN
        [dbo].[employees] e ON e.emp_id = ad.emp_id
    INNER JOIN
        [dbo].[attendance] a ON a.atd_id = ad.atd_id
    WHERE
        a.org_id = @org_id
        AND MONTH(atd_date) = @month
        AND YEAR(atd_date) = @year
    GROUP BY
        e.emp_id,
        e.emp_firstname,
        e.emp_lastname,
        e.emp_hourly_rate;
END;
