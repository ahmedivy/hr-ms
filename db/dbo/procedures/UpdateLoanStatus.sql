CREATE PROCEDURE [dbo].[UpdateLoanStatus]
    @loan_id INT
AS
BEGIN
    UPDATE dbo.loans
    SET loan_status = 'Paid'
    WHERE loan_id = @loan_id
END

DROP PROCEDURE IF EXISTS [dbo].[UpdateLoanStatus]

SELECT * FROM loans

DECLARE @id INT = 101
EXEC [dbo].[UpdateLoanStatus] @id
