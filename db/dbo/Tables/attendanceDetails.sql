CREATE TABLE [dbo].[attendanceDetails]
(
  [atd_id] INT NOT NULL FOREIGN KEY REFERENCES [dbo].[attendance]([atd_id]),
  [emp_id] INT NOT NULL FOREIGN KEY REFERENCES [dbo].[employees]([emp_id]),
  [atd_start_time] DATETIME NOT NULL,
  [atd_end_time] DATETIME NOT NULL,
  PRIMARY KEY ([atd_id], [emp_id])
)
GO