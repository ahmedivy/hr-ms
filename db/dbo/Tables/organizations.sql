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
  [org_country] NVARCHAR(50) NOT NULL,
)
