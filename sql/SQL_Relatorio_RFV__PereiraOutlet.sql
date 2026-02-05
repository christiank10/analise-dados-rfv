-- PASSO 1: CRIAR O BANCO (EXECUTE ESTE BLOCO PRIMEIRO SE QUISER)
USE master;
GO

IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'PereiraOutletDB')
BEGIN
    CREATE DATABASE PereiraOutletDB;
END
GO

-- PASSO 2: ENTRAR NO BANCO CRIADO
USE PereiraOutletDB;
GO

-- PASSO 3: CRIAR A TABELA E OS DADOS
IF OBJECT_ID('Vendas_PereiraOutlet', 'U') IS NOT NULL 
    DROP TABLE Vendas_PereiraOutlet;
GO

CREATE TABLE Vendas_PereiraOutlet (
    ID_Pedido INT PRIMARY KEY IDENTITY(1,1),
    ID_Cliente INT,
    Nome_Cliente VARCHAR(100),
    Data_Venda DATETIME,
    Valor_Total DECIMAL(18,2)
);
GO

INSERT INTO Vendas_PereiraOutlet (ID_Cliente, Nome_Cliente, Data_Venda, Valor_Total)
VALUES 
(1, 'Marcos Oliveira', GETDATE()-3, 450.00),
(2, 'Beatriz Souza', GETDATE()-120, 890.00),
(3, 'Carlos Iago', GETDATE()-10, 120.00),
(4, 'Julia Mendes', GETDATE()-2, 1500.00),
(1, 'Marcos Oliveira', GETDATE()-20, 320.00);
GO

-- PASSO 4: CRIAR A STORED PROCEDURE
CREATE OR ALTER PROCEDURE sp_Relatorio_RFV_PereiraOutlet
AS
BEGIN
    SET NOCOUNT ON;
    WITH Calculo_Base AS (
        SELECT 
            ID_Cliente, Nome_Cliente,
            DATEDIFF(DAY, MAX(Data_Venda), GETDATE()) AS Recencia,
            COUNT(ID_Pedido) AS Frequencia,
            SUM(Valor_Total) AS Valor
        FROM Vendas_PereiraOutlet
        GROUP BY ID_Cliente, Nome_Cliente
    ),
    Ranking AS (
        SELECT *,
            NTILE(5) OVER (ORDER BY Recencia DESC) AS R,
            NTILE(5) OVER (ORDER BY Frequencia ASC) AS F,
            NTILE(5) OVER (ORDER BY Valor ASC) AS V
        FROM Calculo_Base
    )
    SELECT 
        Nome_Cliente, Recencia, Frequencia, Valor, R, F, V,
        CASE 
            WHEN R >= 4 AND F >= 4 THEN 'Fã PereiraOutlet' 
            WHEN R <= 2 THEN 'Risco de Perda'
            ELSE 'Regular' 
        END AS Status_Segmento
    FROM Ranking;
END;
GO

-- PASSO 5: EXECUTAR O TESTE FINAL
EXEC sp_Relatorio_RFV_PereiraOutlet;
GO