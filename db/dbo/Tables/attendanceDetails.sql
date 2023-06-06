DROP TABLE IF EXISTS [dbo].[attendanceDetails]
GO

CREATE TABLE [dbo].[attendanceDetails]
(
  [atd_id] INT NOT NULL FOREIGN KEY REFERENCES [dbo].[attendance]([atd_id]),
  [emp_id] INT NOT NULL FOREIGN KEY REFERENCES [dbo].[employees]([emp_id]),
  [time_in] TIME NOT NULL,
  [time_out] TIME NOT NULL,
  PRIMARY KEY ([atd_id], [emp_id])
)
GO
