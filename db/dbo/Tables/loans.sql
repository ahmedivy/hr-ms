CREATE TABLE [dbo].[loans]
(
  [loan_id] INT IDENTITY(100, 1) NOT NULL PRIMARY KEY,
  [emp_id] INT NOT NULL FOREIGN KEY REFERENCES [dbo].[employees]([emp_id]),
  [loan_amount] MONEY NOT NULL,
  [loan_date] DATETIME NOT NULL,
  [loan_status] NVARCHAR(50) NOT NULL,
  [loan_description] NVARCHAR(100) NOT NULL,
)

ALTER TABLE [dbo].[loans] ADD CONSTRAINT [DF_loans_loan_status] DEFAULT ('Pending') FOR [loan_status]

ALTER TABLE [dbo].[loans] ADD CONSTRAINT [DF_loans_loan_description] DEFAULT ('') FOR [loan_description]

ALTER TABLE [dbo].[loans] ADD CONSTRAINT [DF_loans_loan_date] DEFAULT (GETDATE()) FOR [loan_date]

-- Add payment date field
ALTER TABLE [dbo].[loans] ADD [loan_payment_date] DATETIME NULL
