DROP TABLE IF EXISTS [dbo].[users];
GO


CREATE TABLE [dbo].[users]
(
    [user_id] INT NOT NULL,
    [user_firstname] NCHAR (20) NOT NULL,
    [user_lastname] NCHAR (20) NULL,
    [user_email] NCHAR (50) NULL,
    CONSTRAINT [PK_users] PRIMARY KEY CLUSTERED ([user_id] ASC)
);

GO

-- Delete all rows from organizations table
DELETE FROM [dbo].[organizations];
GO

SELECT *
FROM [dbo].[employees];


SELECT *
FROM [dbo].[attendanceDetails];