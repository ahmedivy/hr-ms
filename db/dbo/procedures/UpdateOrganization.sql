CREATE PROCEDURE dbo.UpdateOrganization
  @id INT,
  @name NVARCHAR(50),
  @email NVARCHAR(50),
  @website NVARCHAR(50),
  @type NVARCHAR(50),
  @phone NVARCHAR(20),
  @city NVARCHAR(100),
  @address NVARCHAR(100),
  @state NVARCHAR(50),
  @country NVARCHAR(50),
  @zip NVARCHAR(20)
AS
BEGIN
  SET NOCOUNT ON;

  -- Update the organization in the database
  UPDATE dbo.Organizations
  SET org_name = @name,
      org_email = @email,
      org_website = @website,
      org_type = @type,
      org_phone = @phone,
      org_city = @city,
      org_address = @address,
      org_state = @state,
      org_country = @country,
      org_zip = @zip
  WHERE org_id = @id;
END
