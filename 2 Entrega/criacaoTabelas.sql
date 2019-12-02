DROP TABLE compra_produto;

DROP TABLE venda_produto;

DROP TABLE venda;

DROP TABLE supervisiona;

DROP TABLE vendedor;

DROP TABLE gerente;

DROP TABLE funcionario;

DROP TABLE compra_entrada;

DROP TABLE telefone_fornecedor;

DROP TABLE fornecedor;

DROP TABLE produto;

DROP TABLE telefone_cliente;

DROP TABLE cliente;

CREATE TABLE funcionario (
    cpf     BIGINT,
    nome    VARCHAR(20),
    email   VARCHAR(30),
    senha   VARCHAR(50),
	flagGerente BOOL,
    PRIMARY KEY ( cpf )
);

CREATE TABLE gerente (
    cpf BIGINT,
    PRIMARY KEY ( cpf ),
    FOREIGN KEY ( cpf ) REFERENCES funcionario ( cpf )
);

CREATE TABLE vendedor (
    cpf           BIGINT,
    cpf_gerente   BIGINT,
    meta          INTEGER,
    PRIMARY KEY ( cpf ),
    FOREIGN KEY ( cpf ) REFERENCES funcionario ( cpf ),
    FOREIGN KEY ( cpf_gerente ) REFERENCES gerente ( cpf )
);

CREATE TABLE supervisiona (
    cpf_gerente    BIGINT,
    cpf_vendedor   BIGINT,
    FOREIGN KEY ( cpf_gerente ) REFERENCES gerente ( cpf ),
    FOREIGN KEY ( cpf_vendedor ) REFERENCES vendedor ( cpf )
);

CREATE TABLE fornecedor (
    cnpj     BIGINT,
    nome     VARCHAR(20),
    email    VARCHAR(30),
    rua      VARCHAR(50),
    numero   INTEGER,
    bairro   VARCHAR(50),
    cidade   VARCHAR(50),
    PRIMARY KEY ( cnpj )
);

CREATE TABLE telefone_fornecedor (
    cnpj_fornecedor   BIGINT,
    telefone          INTEGER,
    PRIMARY KEY ( cnpj_fornecedor, telefone ),
    FOREIGN KEY ( cnpj_fornecedor ) REFERENCES fornecedor ( cnpj )
);

CREATE TABLE produto (
    id_produto     SERIAL,
    nome           VARCHAR(20),
    preco_venda    INTEGER,
    preco_compra   INTEGER,
    qtd_estoque    INTEGER,
    PRIMARY KEY ( id_produto )
);

CREATE TABLE compra_entrada (
    id_entrada        SERIAL,
    cnpj_fornecedor   BIGINT,
    data_compra       DATE,
    valor_total       INTEGER,
    PRIMARY KEY ( id_entrada ),
    FOREIGN KEY ( cnpj_fornecedor ) REFERENCES fornecedor ( cnpj )
);

CREATE TABLE compra_produto (
    id_produto_produto   SERIAL,
    id_entrada_compra      SERIAL,
    quantidade           INTEGER,
    PRIMARY KEY ( id_produto_produto, id_entrada_compra ),
    FOREIGN KEY ( id_produto_produto ) REFERENCES produto ( id_produto ),
    FOREIGN KEY ( id_entrada_compra ) REFERENCES compra_entrada ( id_entrada )
);

CREATE TABLE cliente (
    cpf              BIGINT,
    nome_cliente     VARCHAR(20),
    email_cliente    VARCHAR(20),
    rua_cliente      VARCHAR(50),
    numero_cliente   INTEGER,
    bairro_cliente   VARCHAR(50),
    cidade_cliente   VARCHAR(50),
    PRIMARY KEY ( cpf )
);

CREATE TABLE telefone_cliente (
    cpf_cliente   BIGINT,
    telefone      INTEGER,
    PRIMARY KEY ( cpf_cliente, telefone ),
    FOREIGN KEY ( cpf_cliente ) REFERENCES cliente ( cpf )
);

CREATE TABLE venda (
    id_saida                SERIAL,
    cpf_funcionario_venda   BIGINT,
    cpf_cliente_venda       BIGINT,
    data_venda              DATE,
    valor_total             INTEGER,
    PRIMARY KEY ( id_saida ),
    FOREIGN KEY ( cpf_funcionario_venda ) REFERENCES funcionario ( cpf ),
    FOREIGN KEY ( cpf_cliente_venda ) REFERENCES cliente ( cpf )
);

CREATE TABLE venda_produto (
    id_produto_produto   SERIAL,
    id_saida_venda       SERIAL,
    quantidade           INTEGER,
    PRIMARY KEY ( id_produto_produto, id_saida_venda ),
    FOREIGN KEY ( id_produto_produto ) REFERENCES produto ( id_produto ),
    FOREIGN KEY ( id_saida_venda ) REFERENCES venda ( id_saida )
);
