📊 Sistema de Inteligência de Marketing - PereiraOutlet (RFV)

Este projeto consiste em um ecossistema de dados completo para análise de comportamento de clientes utilizando a metodologia RFV (Recência, Frequência e Valor). O sistema integra um banco de dados SQL Server com automação em Python para gerar dashboards executivos interativos.

🚀 Tecnologias Utilizadas
Banco de Dados: Microsoft SQL Server (Transact-SQL)

Linguagem: Python 3.12

Bibliotecas de Dados: Pandas e NumPy

Visualização: Plotly (Gráficos Interativos) e Bootstrap (Layout Web)

Conectividade: PyODBC

🧠 O que é a Análise RFV?
O objetivo deste projeto para a PereiraOutlet é segmentar a base de clientes automaticamente para direcionar campanhas de marketing:

Recência (R): Há quanto tempo o cliente comprou? (Quanto mais recente, melhor).

Frequência (F): Quantas vezes ele comprou no período?

Valor (V): Quanto ele gastou no total?

Segmentos Identificados:

Fã PereiraOutlet (VIP): Compra muito, gasta bem e comprou recentemente.

Cliente de Ocasião: Compra pouco, mas gasta valores altos.

Hibernando/Risco de Perda: Clientes que não compram há muito tempo.

🛠️ Como Executar o Projeto
1. Banco de Dados
Execute o script em sql/sp_relatorio_rfv.sql no seu SQL Server para criar a estrutura de tabelas e a Stored Procedure que processa o ranking dos clientes.

2. Ambiente Python
Recomenda-se o uso de ambiente virtual:

Bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
3. Geração do Dashboard
Rode o script principal:

Bash
python sistema_rfv_web_v2.py
📈 Resultados
O sistema gera automaticamente um arquivo dashboard_pereira_outlet.html com visualização em Dark Mode, contendo gráficos de distribuição e tabelas detalhadas.

Dica: Insira aqui o print do seu Dashboard no navegador para mostrar o resultado final!

👤 Autor
Christian Luiz LinkedIn: [https://www.linkedin.com/in/christian-luiz-36056b155/] 

Dica de ouro para o seu GitHub:
Crie um arquivo requirements.txt: Digite pip freeze > requirements.txt no terminal para que outros possam instalar as bibliotecas que você usou com um único comando.

Organização: No seu GitHub, faça o upload da pasta sql e da pasta scripts separadamente para ficar bem organizado.
