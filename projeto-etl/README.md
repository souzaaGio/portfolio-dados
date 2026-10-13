# Projeto Pipeline ETL Simples (Python + Pandas + SQLite)

Projeto prático de Engenharia de Dados para iniciantes, desenvolvido do zero para aprender a manipular tabelas e bancos de dados em Python.

O script simula o ciclo completo de um processo **ETL** (Extract, Transform, Load): pega dados brutos e desorganizados de vendas, aplica regras de limpeza e salva o resultado em um banco de dados relacional.

## Tecnologias

* Python
* Pandas (manipulação de tabelas/DataFrames)
* SQLite3 (banco de dados relacional nativo do Python)
* VS Code

## O que o código faz

1. **Extração:** cria uma tabela (DataFrame) a partir de dados de vendas intencionalmente bagunçados (nomes fora de padrão, preços como texto e valores nulos).
2. **Transformação:**
   * substitui valores nulos em `quantidade` por `1` (`.fillna()`)
   * padroniza os nomes dos clientes (`.str.title()`)
   * limpa a coluna `preco`: remove "R$ " e pontos de milhar, troca a vírgula por ponto e converte para número (`float`)
   * cria a coluna calculada `valor_total` (preço x quantidade)
3. **Carga:** salva os dados tratados na tabela `relatorio_vendas` de um banco SQLite.
4. **Consulta:** roda um `SELECT * FROM relatorio_vendas` para conferir os dados salvos.

## Como rodar

1. Instale o Pandas:
   `python -m pip install pandas`
2. Dentro da pasta `projeto-etl`, execute:
   `python main.py`

O arquivo do banco (`meu_banco_seguro.db`) é criado automaticamente ao rodar.
