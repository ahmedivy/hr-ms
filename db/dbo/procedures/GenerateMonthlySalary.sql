CREATE PROCEDURE GenerateMonthlySalary
  @org_id INT,
  @month NVARCHAR(10),
  @year NVARCHAR(4)
AS
BEGIN
  -- Step 1: Insert salary row
  DECLARE @sal_id INT;

  INSERT INTO [dbo].[salary]
    ([org_id], [sal_created_date], [sal_month], [sal_year], [sal_discription])
  VALUES
    (@org_id, GETDATE(), @month, @year, NULL);

  SET @sal_id = SCOPE_IDENTITY();

  -- Step 2: Insert salary details for each employee
  INSERT INTO [dbo].[salaryDetails]
    ([sal_id], [emp_id], [sal_gross_amount], [sal_deductions], [sal_net_amount])
  SELECT
    @sal_id,
    e.emp_id,
    SUM(DATEDIFF(HOUR, ad.time_in, ad.time_out)) * e.emp_hourly_rate AS 'sal_gross_amount',
    0.00 AS 'sal_deductions',
    SUM(DATEDIFF(HOUR, ad.time_in, ad.time_out)) * e.emp_hourly_rate AS 'sal_net_amount'
  FROM
    [dbo].[attendanceDetails] ad
    INNER JOIN
    [dbo].[employees] e ON e.emp_id = ad.emp_id
    INNER JOIN
    [dbo].[attendance] a ON a.atd_id = ad.atd_id
  WHERE
        a.org_id = @org_id
    AND MONTH(a.atd_date) = MONTH(CAST(@year + '-' + @month + '-01' AS DATE))
    AND YEAR(a.atd_date) = @year
  GROUP BY
        e.emp_id,
        e.emp_hourly_rate;
END;

EXEC GenerateMonthlySalary 109, 'November', '2021';