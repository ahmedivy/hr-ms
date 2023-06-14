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
  [emp_hourly_rate] MONEY NOT NULL,
)
GO

-- Adding CNIC column
ALTER TABLE [dbo].[employees]
ADD [emp_cnic] NVARCHAR(20) NULL
GO

SELECT TOP(1) * FROM Employees

-- add default for hire date
ALTER TABLE [dbo].[employees]
ADD CONSTRAINT [DF_employees_emp_hire_date] DEFAULT (GETDATE()) FOR [emp_hire_date]

-- Set DOB to allow nulls
ALTER TABLE [dbo].[employees]
ALTER COLUMN [emp_dob] DATE NULL

-- EMAIL Validation Constraint
ALTER TABLE [dbo].[employees]
ADD CONSTRAINT [CK_employees_emp_email] CHECK (emp_email LIKE '%_@__%.__%')

ALTER TABLE [dbo].[employees]
ALTER COLUMN [emp_email] NVARCHAR(50) NOT NULL

-- CNIC Unique Constraint
ALTER TABLE [dbo].[employees]
ADD CONSTRAINT [UQ_employees_emp_cnic] UNIQUE ([emp_cnic])

-- CNIC Validation Constraint
ALTER TABLE [dbo].[employees]
ADD CONSTRAINT [CK_employees_emp_cnic] CHECK (emp_cnic LIKE '[0-9][0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9][0-9]-[0-9]')

-- Phone Validation Constraint
ALTER TABLE [dbo].[employees]
ADD CONSTRAINT [CK_employees_emp_phone] CHECK (emp_phone LIKE '[0-9][0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9][0-9]')