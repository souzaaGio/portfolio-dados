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
