-- Procdure to get employees by organization.
-- @organizationId: The organization id.
-- Returns: The employees.

DROP PROCEDURE IF EXISTS [dbo].[getEmployees]
GO

CREATE PROCEDURE [dbo].[getEmployees]
  @org_id int = NULL
AS
BEGIN
  SET NOCOUNT ON;

  IF @org_id IS NULL
    SELECT *
  FROM [dbo].[employees]
  ELSE
    SELECT *
  FROM [dbo].[employees]
  WHERE [org_id] = @org_id
END

GO
