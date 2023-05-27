IF NOT EXISTS (SELECT 1
FROM sys.tables
WHERE name = 'organizations' AND schema_id = SCHEMA_ID('dbo'))
BEGIN
  CREATE TABLE [dbo].[organizations]
  (
    [org_id] INT IDENTITY(100, 1) NOT NULL PRIMARY KEY,
    [org_name] NVARCHAR(50) NOT NULL,
    [org_description] NVARCHAR(100) NOT NULL,
    [org_type] NVARCHAR(50) NOT NULL,
    [org_phone] NVARCHAR(20) NOT NULL,
    [org_email] NVARCHAR(50) NOT NULL,
    [org_website] NVARCHAR(50) NOT NULL,
    [org_logo_url] NVARCHAR(50) NOT NULL,
    [org_registration_date] DATETIME NOT NULL,
    [org_address] NVARCHAR(100) NOT NULL,
    [org_city] NVARCHAR(50) NOT NULL,
    [org_state] NVARCHAR(50) NOT NULL,
    [org_zip] NVARCHAR(50) NOT NULL,
    [org_country] NVARCHAR(50) NOT NULL
  );
END


-- Adding default value for org_registration_date
ALTER TABLE [dbo].[organizations] ADD CONSTRAINT [DF_organizations_org_registration_date] DEFAULT (GETDATE()) FOR [org_registration_date]

-- Changing description, type, website, logo_url, address, city, state, zip, country to allow nulls
ALTER TABLE [dbo].[organizations] ALTER COLUMN [org_description] NVARCHAR(100) NULL
ALTER TABLE [dbo].[organizations] ALTER COLUMN [org_type] NVARCHAR(50) NULL
ALTER TABLE [dbo].[organizations] ALTER COLUMN [org_website] NVARCHAR(50) NULL
ALTER TABLE [dbo].[organizations] ALTER COLUMN [org_logo_url] NVARCHAR(50) NULL
ALTER TABLE [dbo].[organizations] ALTER COLUMN [org_address] NVARCHAR(100) NULL
ALTER TABLE [dbo].[organizations] ALTER COLUMN [org_city] NVARCHAR(30) NULL
ALTER TABLE [dbo].[organizations] ALTER COLUMN [org_state] NVARCHAR(30) NULL
ALTER TABLE [dbo].[organizations] ALTER COLUMN [org_zip] NVARCHAR(30) NULL
ALTER TABLE [dbo].[organizations] ALTER COLUMN [org_country] NVARCHAR(30) NULL
