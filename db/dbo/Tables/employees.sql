CREATE TABLE [dbo].[employees]
(
  [emp_id] INT NOT NULL PRIMARY KEY,
  [emp_firstname] NCHAR(20) NOT NULL,
  [emp_lastname] NCHAR(20) NULL,
  [emp_email] NCHAR(50) NULL,
)
