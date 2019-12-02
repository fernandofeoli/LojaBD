from model import connection as conexao
class Compra(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def insereCompra(self, compra):
        try:        
            procValores = (compra.cpfFuncionario, compra.cnpjFornecedor, compra.dataCompra)
            conexao = conexao.Connection()
            conexao.callProCedure(self, "insere_compra" , procValores)
            codCompra = conexao.cur.fetchone()
            
            procValores = None
            for produto in compra.produtosCompra:
                procValores = (produto.id, codCompra, produto.quantidade)
                conexao.execute('INSERT INTO compra_produto(id_produto_produto, id_entrada_compra, quantidade) VALUES(%s,%s,%s)', procValores)
                
            conexao.commit()
        except (Exception, conexao.psycopg2.DatabaseError) as error:
            conexao.rollback()
            print(error)
        finally:
            if conexao is not None:
                conexao.close()
    
    def retornaCompras(self):
        conexao = conexao.Connection()
        print('')
        conexao.query('SELECT * FROM compra_entrada')
        conexao.queryResult()
        conexao.close()

    def relatComprasPeriodo(self, dataInicial, dataFinal):
        conexao = conexao.Connection()
        params = (dataInicial, dataFinal)
        conexao.execute('''SELECT * FROM compra_entrada 
                            WHERE data_compra BETWEEN %s 
                            AND %s ''', params)
        conexao.queryResult()
        conexao.close()
    
    def relatComprasFornecedorPeriodo(self, dataInicial, dataFinal, cnpjFornecedor):
        conexao = conexao.Connection()
        params = (dataInicial, dataFinal, cnpjFornecedor)
        conexao.execute('''SELECT * FROM compra_entrada 
                            WHERE data_compra BETWEEN %s 
                            AND %s 
                            AND cnpj_fornecedor = %s''', params)
        conexao.queryResult()
        conexao.close()