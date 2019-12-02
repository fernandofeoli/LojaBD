CREATE OR REPLACE FUNCTION verifica_meta_vendedor (IN cpf_vendedor BIGINT, IN mes INTEGER, IN ano INTEGER)
    RETURNS VARCHAR AS $$
DECLARE
    resultado_meta VARCHAR(20);
    meta_vendedor INTEGER;
    valor_vendas INTEGER;
BEGIN
    SELECT meta INTO meta_vendedor
    FROM vendedor
    WHERE vendedor.cpf = cpf_vendedor;
    
    SELECT SUM(valor_total) INTO valor_vendas
    FROM venda
    WHERE venda.cpf_funcionario_venda = cpf_vendedor
    AND CAST((extract(month from venda.data_venda)) AS INTEGER) = mes
	AND CAST((extract(year from venda.data_venda)) AS INTEGER) = ano;
    
    IF valor_vendas >= meta_vendedor THEN
        resultado_meta := 'Meta atingida';
    ELSE
        resultado_meta := 'Meta não atingida';
    END IF;
	RETURN resultado_meta;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION insere_venda (IN cpf_funcionario BIGINT, IN cpf_cliente BIGINT, IN data_venda DATE, IN total INTEGER)
	RETURNS INTEGER AS $$
DECLARE
	lastIDsaida INTEGER;
	newIDsaida INTEGER;
BEGIN 
	SELECT max(id_saida) FROM venda INTO lastIDsaida;
	newIDsaida := lastIDsaida +1;
	INSERT INTO venda VALUES (newIDsaida,cpf_funcionario,cpf_cliente,data_venda,total);
	RETURN newIDsaida;
END; 
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION insere_compra (IN cnpj_fornecedor BIGINT, IN data_compra DATE, IN total INTEGER)
	RETURNS INTEGER AS $$
DECLARE
	lastIdEntrada INTEGER;
	newIdEntrada INTEGER;
BEGIN 
	SELECT max(id_entrada) FROM compra_entrada INTO lastIdEntrada;
	newIdEntrada := lastIdEntrada +1;
	INSERT INTO compra_entrada VALUES (newIdEntrada,cnpj_fornecedor,data_compra,total);
	RETURN newIdEntrada;
END; 
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION verifica_supervisor(IN cpf_vendedor BIGINT)
	RETURNS VARCHAR(50) AS $$
DECLARE 
	cpf_supervisor BIGINT;
	nome_supervisor VARCHAR(20);
	supervisor VARCHAR(30);
BEGIN
	SELECT cpf_gerente INTO cpf_supervisor
	FROM vendedor 
	WHERE cpf = cpf_vendedor;
	
	IF cpf_supervisor = NULL THEN 
		RAISE EXCEPTION 'Não foi encontrado um supervisor para o vendedor em questão!';
	ELSE
		SELECT nome INTO nome_supervisor
		FROM funcionario 
		WHERE cpf = cpf_supervisor;
	END IF;
		
	supervisor := CONCAT(CAST(cpf_supervisor AS VARCHAR),' ' ,nome_supervisor);
	RETURN supervisor;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION verifica_supervisionados(IN p_cpf_gerente BIGINT)
	RETURNS TABLE(cpf BIGINT, nome VARCHAR(20)) AS $$
BEGIN
	RETURN QUERY 
	SELECT f.cpf, f.nome
	FROM gerente gt 
	INNER JOIN vendedor v on gt.cpf = v.cpf_gerente
	INNER JOIN funcionario f on v.cpf = f.cpf
	WHERE gt.cpf = p_cpf_gerente;
	
	RETURN;
END;
$$ LANGUAGE plpgsql;
