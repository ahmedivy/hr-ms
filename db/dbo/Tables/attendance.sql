CREATE TABLE [dbo].[attendance]
(
  [atd_id] INT IDENTITY(100, 1) NOT NULL PRIMARY KEY,
  [org_id] INT NOT NULL FOREIGN KEY REFERENCES [dbo].[organizations]([org_id]),
  [atd_date] DATE NOT NULL,
)


CREATE NONCLUSTERED INDEX [IX_atd_date]
ON [dbo].[attendance] ([atd_date] ASC)