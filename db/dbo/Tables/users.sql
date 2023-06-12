DROP TABLE IF EXISTS [dbo].[users];
GO


CREATE TABLE [dbo].[users]
(
    [user_id] INT NOT NULL,
    [user_firstname] NCHAR (20) NOT NULL,
    [user_lastname] NCHAR (20) NULL,
    [user_email] NCHAR (50) NULL,
    CONSTRAINT [PK_users] PRIMARY KEY CLUSTERED ([user_id] ASC)
);

GO

-- Delete all rows from organizations table
DELETE FROM [dbo].[organizations];
GO

SELECT *
FROM [dbo].[employees];


SELECT *
FROM [dbo].[attendanceDetails];

SELECT *
FROM loans;

INSERT INTO dbo.loans
    (emp_id, loan_amount, loan_description)
VALUES
    (169, 400, '')


SELECT *
FROM employees

UPDATE employees
SET emp_hourly_rate = FLOOR(RAND(CHECKSUM(NEWID()))*(250-100+1)+100)


SELECT a.atd_date, e.emp_firstname, e.emp_hourly_rate,
SUM(DATEDIFF(HOUR, ad.time_in, ad.time_out)) AS 'Total Hours',
SUM(DATEDIFF(HOUR, ad.time_in, ad.time_out)) * e.emp_hourly_rate AS 'Total Pay'
FROM [dbo].[attendanceDetails] ad
INNER JOIN [dbo].[employees] e ON e.emp_id = ad.emp_id
INNER JOIN [dbo].[attendance] a ON a.atd_id = ad.atd_id
WHERE a.org_id = 106 and MONTH(atd_date) = MONTH(CAST('2021' + '-' + 'January' + '-01' AS DATE)) and YEAR(atd_date) = YEAR(CAST('2021' + '-' + 'January' + '-01' AS DATE))
AND e.emp_firstname = 'Paco'
GROUP BY ad.atd_id, e.emp_firstname, e.emp_hourly_rate, a.atd_date;
GO


CREATE PROCEDURE GetMonthlyAttendance
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


EXEC GetMonthlyAttendance 106, 2, 2021;
GO



EXEC GenerateSalary 106, 'February', '2021';

SELECT * FROM salaryDetails WHERE sal_id = 108

SELECT * FROM employees WHERE emp_firstname = 'Ahmad'

UPDATE Loans SET loan_status = 'Paid' WHERE loan_id = 107

SELECT * FROM loans WHERE loan_id = 107