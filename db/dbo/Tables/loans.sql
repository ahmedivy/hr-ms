CREATE TABLE [dbo].[loans]
(
  [loan_id] INT IDENTITY(100, 1) NOT NULL PRIMARY KEY,
  [emp_id] INT NOT NULL FOREIGN KEY REFERENCES [dbo].[employees]([emp_id]),
  [loan_amount] MONEY NOT NULL,
  [loan_date] DATETIME NOT NULL,
  [loan_status] NVARCHAR(50) NOT NULL,
  [loan_description] NVARCHAR(100) NOT NULL,
)
