CREATE TABLE [dbo].[salaryDetails]
(
  [sal_id] INT NOT NULL FOREIGN KEY REFERENCES [dbo].[salary]([sal_id]),
  [emp_id] INT NOT NULL FOREIGN KEY REFERENCES [dbo].[employees]([emp_id]),
  [sal_gross_amount] MONEY NOT NULL,
  [sal_deductions] MONEY NOT NULL,
  [sal_net_amount] MONEY NOT NULL,
  PRIMARY KEY ([sal_id], [emp_id])
)
