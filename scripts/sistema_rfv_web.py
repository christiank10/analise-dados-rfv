import pyodbc
import pandas as pd
import plotly.express as px

# 1. CONFIGURAÇÃO DA CONEXÃO (Baseado nas suas fotos)
server = r'DESKTOP-B5U4T25\SQLEXPRESS'
database = 'PereiraOutletDB'
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

try:
    # Conectando ao Banco
    conn = pyodbc.connect(conn_str)
    print("Conexão com PereiraOutletDB realizada com sucesso!")

    # Buscando os dados da Procedure
    query = "EXEC sp_Relatorio_RFV_PereiraOutlet"
    df = pd.read_sql(query, conn)

    # 2. CRIAÇÃO DO GRÁFICO (Plotly Dark Theme)
    contagem_segmentos = df['Segmentacao_Outlet'].value_counts().reset_index()
    contagem_segmentos.columns = ['Segmento', 'Quantidade']

    fig = px.bar(contagem_segmentos, 
                 x='Segmento', 
                 y='Quantidade',
                 title='Análise de Segmentos - PereiraOutlet',
                 color='Segmento',
                 color_discrete_sequence=px.colors.qualitative.Pastel,
                 template='plotly_dark')

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=50, b=20)
    )

    graph_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    # 3. CRIAÇÃO DA TABELA HTML
    table_html = df.to_html(classes='table table-hover', index=False)

    # 4. O NOVO STYLE (HTML + CSS)
    html_final = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dashboard Executivo | PereiraOutlet</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
        <style>
            :root {{
                --bg-color: #0f111a;
                --card-bg: #161b22;
                --accent-color: #58a6ff;
                --text-main: #c9d1d9;
            }}
            body {{ 
                background-color: var(--bg-color); 
                color: var(--text-main); 
                padding: 40px 20px; 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            }}
            .container {{ 
                max-width: 1100px; 
                background: var(--card-bg); 
                padding: 30px; 
                border-radius: 20px; 
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                border: 1px solid #30363d;
            }}
            h1 {{ 
                color: var(--accent-color); 
                font-weight: 700;
                text-align: center; 
                margin-bottom: 10px;
                text-transform: uppercase;
                letter-spacing: 2px;
            }}
            p.subtitle {{
                text-align: center;
                color: #8b949e;
                margin-bottom: 40px;
            }}
            .graph-container {{
                background: #0d1117;
                border-radius: 15px;
                padding: 15px;
                margin-bottom: 40px;
                border: 1px solid #30363d;
            }}
            h3 {{
                color: var(--accent-color);
                border-left: 5px solid var(--accent-color);
                padding-left: 15px;
                margin-bottom: 20px;
                font-size: 1.2rem;
            }}
            /* Estilização da Tabela */
            .table-responsive {{
                border-radius: 10px;
                overflow: hidden;
            }}
            table {{ 
                color: var(--text-main) !important; 
                border-collapse: separate;
                border-spacing: 0;
            }}
            .table thead th {{
                background-color: #21262d !important;
                color: var(--accent-color) !important;
                border-bottom: 2px solid #30363d;
                text-transform: uppercase;
                font-size: 0.85rem;
            }}
            .table-hover tbody tr:hover {{
                background-color: #1f242c !important;
                transition: 0.3s;
            }}
            .table td {{
                border-bottom: 1px solid #30363d;
                vertical-align: middle;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Dashboard PereiraOutlet</h1>
            <p class="subtitle">Relatório de Inteligência RFV - Gerado via Python & SQL Server</p>
            
            <div class="graph-container">
                {graph_html}
            </div>

            <h3>Detalhamento da Base de Clientes</h3>
            <div class="table-responsive">
                {table_html}
            </div>
        </div>
    </body>
    </html>
    """

    # Salvando o arquivo
    with open("dashboard_pereira_outlet.html", "w", encoding="utf-8") as f:
        f.write(html_final)

    print("\n✅ Dashboard Estilizado criado com sucesso: 'dashboard_pereira_outlet.html'")

except Exception as e:
    print(f"❌ Erro ao gerar o Dashboard: {e}")