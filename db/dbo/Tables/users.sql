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

SELECT * FROM loans;

INSERT INTO dbo.loans (emp_id, loan_amount, loan_description) VALUES (169, 400,'')


SELECT * FROM employees

UPDATE employees
SET emp_hourly_rate = FLOOR(RAND(CHECKSUM(NEWID()))*(250-100+1)+100)
