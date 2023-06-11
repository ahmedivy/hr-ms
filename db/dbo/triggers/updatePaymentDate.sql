
CREATE TRIGGER [dbo].[UpdateLoanPaymentDate]
ON [dbo].[loans]
AFTER UPDATE
AS
BEGIN
    IF UPDATE([loan_status])
    BEGIN
        UPDATE [dbo].[loans]
        SET [loan_payment_date] = GETDATE()
        FROM [dbo].[loans] l
        INNER JOIN inserted i ON l.[loan_id] = i.[loan_id]
        WHERE i.[loan_status] = 'Paid'
    END
END;