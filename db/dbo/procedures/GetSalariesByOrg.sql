CREATE PROCEDURE [dbo].[GetSalariesByOrg]
  @org_id INT
AS
BEGIN
  SELECT
    s.sal_id,
    s.sal_month + ' (' + s.sal_year + ')' AS sal_month,
    SUM(sd.sal_gross_amount) AS total_gross,
    SUM(sd.sal_deductions) AS total_deductions,
    SUM(sd.sal_net_amount) AS total_net
  FROM [dbo].[salary] s
    JOIN [dbo].[salaryDetails] sd ON s.sal_id = sd.sal_id
  WHERE s.org_id = @org_id
  GROUP BY s.sal_id, s.sal_month, s.sal_year
END