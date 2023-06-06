CREATE PROCEDURE [dbo].[GetOrganizationDetails]
  @id int
AS
BEGIN
  SELECT *
  FROM dbo.organizations
  WHERE org_id = @id
END
GO

EXECUTE [dbo].[GetOrganizationDetails] @id = 106