DROP PROCEDURE IF EXISTS [dbo].[GetLoans]
GO

CREATE PROCEDURE [dbo].[GetLoans]
  @org_id INT
AS
BEGIN
  SELECT
    e.emp_id AS emp_id,
    e.emp_firstname + ' ' + e.emp_lastname AS emp_name,
    o.org_id AS org_id,
    o.org_name AS org_name,
    l.loan_id AS loan_id,
    l.loan_amount AS loan_amount,
    l.loan_date AS loan_date,
    l.loan_status AS loan_status,
    l.loan_description AS loan_description,
    l.loan_payment_date AS loan_payment_date
  FROM [dbo].[loans] l
    INNER JOIN [dbo].[employees] e ON l.emp_id = e.emp_id
    INNER JOIN [dbo].[organizations] o ON e.org_id = o.org_id
  WHERE o.org_id = @org_id
END
GO