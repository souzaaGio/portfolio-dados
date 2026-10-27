# Análise de Vendas de E-commerce

Pipeline em Python que lê dados de clientes e pedidos, junta as duas tabelas e calcula a receita por cidade.

**Pergunta de negócio:** qual cidade gera mais receita?

**Resposta:** Rio de Janeiro, com R$ 3.930 em vendas.

## Dados
- `clientes.csv`: id, nome e cidade de cada cliente.
- `pedidos.csv`: cada compra, com data, produto e valor.

## O que o código faz
1. Lê os dois arquivos com Pandas.
2. Junta cada pedido com o cliente dono dele (`merge`).
3. Soma a receita por cidade (`groupby` + `sum`).
4. Salva o resultado num banco SQLite (`ecommerce.db`).

## Como rodar
1. Instale o Pandas: `python -m pip install pandas`
2. Na pasta `ecommerce`, execute: `python analise.py`