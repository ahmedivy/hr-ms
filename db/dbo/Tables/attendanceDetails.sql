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


ALTER TABLE [dbo].[attendanceDetails]
ADD CONSTRAINT [CK_attendanceDetails_time_in] CHECK ([time_in] >= '00:00:00' AND [time_in] <= '23:59:59')

ALTER TABLE [dbo].[attendanceDetails]
ADD CONSTRAINT [CK_attendanceDetails_time_out] CHECK ([time_out] >= '00:00:00' AND [time_out] <= '23:59:59')
