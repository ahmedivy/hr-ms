ALTER PROCEDURE [dbo].[GetOrganizationDetails]
  @id int
AS
BEGIN
  SELECT org_id, org_name, org_description, org_type, org_phone, org_email, org_website, org_logo_url, org_registration_date, org_address, org_city, org_state, org_zip, org_country
  FROM dbo.organizations
  WHERE org_id = @id
END
GO

EXECUTE [dbo].[GetOrganizationDetails] @id = 106