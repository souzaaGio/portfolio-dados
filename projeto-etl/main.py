# 1. Avisamos o Python que vamos usar o Pandas e damos o apelido de 'pd'
import pandas as pd
import sqlite3

print("=== INICIANDO O PROJETO ETL ===")

# 2. Criamos um dicionário comum com os dados bagunçados da nossa loja
tabela = pd.read_csv("vendas_sujas.csv")
print(tabela)

tabela["quantidade"] = tabela["quantidade"].fillna(1)
print("---Depois da limpeza---")
print(tabela)

tabela["cliente"] = tabela["cliente"].str.title()
print("\n---NOME DS CLIENTES PADRONIZADOS---")
print(tabela)

tabela["preco"] = tabela["preco"].str.replace("R$ ", "", regex=False)
tabela["preco"] = tabela["preco"].str.replace(".", "", regex=False)
tabela["preco"] = tabela["preco"].str.replace(",", ".", regex=False)

tabela["preco"] = tabela["preco"].astype(float)
print("\n--- PREÇOS TOTALMENTE LIMPOS E NUMÉRICOS ---")
print(tabela)

tabela["valor_total"] = tabela["preco"] * tabela["quantidade"]
print("\n=== ETAPA DE TRANSFORMAÇÃO CONCLUÍDA COM SUCESSO! ===")
print(tabela)



print("\n--- PASSO 3: CARGA (SALVANDO OS DADOS) ---")

conexao = sqlite3.connect("meu_banco_seguro.db")
tabela.to_sql("relatorio_vendas", conexao, if_exists="replace", index=False)
conexao.close()

print("\n--- FAZENDO UMA CONSULTA SQL NO BANCO ---")

conexao = sqlite3.connect("meu_banco_seguro.db")
dados_lidos_do_banco = pd.read_sql_query("SELECT * FROM relatorio_vendas", conexao)
conexao.close()
print(dados_lidos_do_banco)
print("\n=== PIPELINE FINALIZADO COM SUCESSO! ===")