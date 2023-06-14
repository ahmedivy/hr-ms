CREATE TABLE [dbo].[salary]
(
  [sal_id] INT IDENTITY(100, 1) NOT NULL PRIMARY KEY,
  [org_id] INT NOT NULL FOREIGN KEY REFERENCES [dbo].[organizations]([org_id]),
  [sal_created_date] DATE NOT NULL,
  [sal_month] NVARCHAR(10) NOT NULL,
  [sal_year] NVARCHAR(4) NOT NULL,
  [sal_discription] NVARCHAR(100) NULL,
)

-- ADD Constaints

ALTER TABLE [dbo].[salary] ADD CONSTRAINT [CK_salary_sal_month] CHECK ([sal_month] IN ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'))