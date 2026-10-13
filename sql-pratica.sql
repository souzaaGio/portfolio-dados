-- Minha prática de SQL

CREATE TABLE clientes (nome TEXT, cidade TEXT);

INSERT INTO clientes VALUES ('Ana', 'Rio de Janeiro');
INSERT INTO clientes VALUES ('Bruno', 'Paracambi');
INSERT INTO clientes VALUES ('maria', 'vassouras');

-- Filtrar com WHERE
SELECT * FROM clientes WHERE cidade = 'Paracambi';

-- Contar
SELECT COUNT(*) FROM clientes;

-- Agrupar: quantos clientes por cidade
SELECT cidade, COUNT(*) FROM clientes GROUP BY cidade;

-- JOIN: juntar clientes e pedidos
DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS pedidos;

CREATE TABLE clientes (id INTEGER, nome TEXT);
INSERT INTO clientes VALUES (1, 'Ana');
INSERT INTO clientes VALUES (2, 'Bruno');

CREATE TABLE pedidos (id INTEGER, cliente_id INTEGER, produto TEXT);
INSERT INTO pedidos VALUES (1, 1, 'bolo');
INSERT INTO pedidos VALUES (2, 1, 'pão');
INSERT INTO pedidos VALUES (3, 2, 'bolo');

SELECT clientes.nome, pedidos.produto FROM pedidos JOIN clientes ON pedidos.cliente_id = clientes.id;
SELECT clientes.nome, pedidos.produto FROM pedidos JOIN clientes ON pedidos.cliente_id = clientes.id WHERE clientes.nome = 'Ana';
