CREATE PROCEDURE GetSalaryDetails
    @sal_id INT
AS
BEGIN
    SELECT
        sd.emp_id,
        CONCAT(e.emp_firstname, ' ', e.emp_lastname) AS emp_name,
        sd.sal_gross_amount AS 'Gross Salary',
        sd.sal_net_amount AS 'Net Salary',
        sd.sal_deductions AS 'Deductions'
    FROM
        [dbo].[salaryDetails] sd
    INNER JOIN
        [dbo].[employees] e ON e.emp_id = sd.emp_id
    INNER JOIN
        [dbo].[salary] s ON s.sal_id = sd.sal_id
    WHERE
        sd.sal_id = @sal_id;
END;

EXEC GetSalaryDetails 100;
