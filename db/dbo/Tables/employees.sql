DROP TABLE IF EXISTS [dbo].[employees]
GO

CREATE TABLE [dbo].[employees]
(
  [emp_id] INT IDENTITY(100, 1) NOT NULL PRIMARY KEY,
  [org_id] INT NOT NULL FOREIGN KEY REFERENCES [dbo].[organizations]([org_id]),
  [emp_firstname] NVARCHAR(20) NOT NULL,
  [emp_lastname] NVARCHAR(20) NULL,
  [emp_email] NVARCHAR(50) NOT NULL,
  [emp_phone] NVARCHAR(20) NOT NULL,
  [emp_address] NVARCHAR(100) NULL,
  [emp_city] NVARCHAR(50) NULL,
  [emp_state] NVARCHAR(50) NULL,
  [emp_zip] NVARCHAR(50) NULL,
  [emp_country] NVARCHAR(50) NULL,
  [emp_hire_date] DATE NOT NULL,
  [emp_termination_date] DATE DEFAULT NULL,
  [emp_dob] DATE NOT NULL,
  [emp_position] NVARCHAR(50) NOT NULL,
  [emp_hourly_rate] DECIMAL(10, 2) NOT NULL,
)
