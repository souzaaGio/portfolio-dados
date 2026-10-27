import pandas as pd
import sqlite3

#1. leitura de dados
clientes = pd.read_csv("clientes.csv")
pedidos = pd.read_csv("pedidos.csv")

#2. junçao: cada pedido recebe os dados do cliente
juntas = pd.merge(pedidos, clientes, left_on="cliente_id", right_on="id")

#3. Pergunta de negócio: receita total por cidade
print(juntas.groupby("cidade")["valor"].sum())

# 4. Salvar no banco SQLite
conexao = sqlite3.connect("ecommerce.db")
juntas.to_sql("vendas_completas", conexao, if_exists="replace", index=False)
conexao.close()

# 5. Conferência
conexao = sqlite3.connect("ecommerce.db")
consulta = pd.read_sql_query("select * FROM vendas_completas", conexao)
print(consulta)
