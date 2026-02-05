import pyodbc
import pandas as pd

# Dados da conexão que vi nas suas fotos
server = r'DESKTOP-B5U4T25\SQLEXPRESS'
database = 'PereiraOutletDB'

conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

try:
    conn = pyodbc.connect(conn_str)
    print("Conexão com PereiraOutletDB realizada com sucesso!")

    # Executa a Stored Procedure
    query = "EXEC sp_Relatorio_RFV_PereiraOutlet"
    df = pd.read_sql(query, conn)

    # Exibe os dados no terminal do VS Code
    print("\n--- Segmentação de Clientes PereiraOutlet ---")
    print(df[['Nome_Cliente', 'Segmentacao_Outlet']])

    # BÔNUS: Salva um arquivo Excel automaticamente
    df.to_excel("relatorio_rfv_final.xlsx", index=False)
    print("\nPlanilha Excel gerada com sucesso!")

except Exception as e:
    print(f"Erro ao conectar ou processar: {e}")