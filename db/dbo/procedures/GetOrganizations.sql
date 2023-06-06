CREATE PROCEDURE GetOrganizations
AS
BEGIN
  SELECT
    org.org_id,
    org.org_name,
    org.org_phone,
    org.org_email,
    org.org_city + ', ' + org.org_country AS org_location,
    COUNT(emp.emp_id) AS total_employees
  FROM
    dbo.organizations AS org
    LEFT JOIN
    dbo.employees AS emp ON org.org_id = emp.org_id
  GROUP BY
    org.org_id,
    org.org_name,
    org.org_phone,
    org.org_email,
    org.org_city,
    org.org_country;
END
GO



