DROP PROCEDURE  IF EXISTS CreateOrganization
GO

CREATE PROCEDURE dbo.CreateOrganization
  @name NVARCHAR(50),
  @email NVARCHAR(50),
  @type NVARCHAR(50),
  @phone NVARCHAR(20),
  @city NVARCHAR(100),
  @address NVARCHAR(100),
  @state NVARCHAR(50),
  @country NVARCHAR(50),
  @zip NVARCHAR(20)
AS
BEGIN
  -- Insert the organization into the database
  INSERT INTO dbo.Organizations
    (org_name, org_email, org_type, org_phone, org_city, org_address, org_state, org_country, org_zip)
  VALUES
    (@name, @email, @type, @phone, @city, @address, @state, @country, @zip);
END
GO

