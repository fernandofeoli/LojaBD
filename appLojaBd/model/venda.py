from model import connection as conexao
class Venda(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def insereVenda(self, venda):
        try:        
            procValores = (venda.cpfFuncionario, venda.cpfCliente, venda.dataVenda, venda.valorTotal)
            conexao = conexao.Connection()
            conexao.callProCedure(self, "insere_venda" , procValores)
            codVenda = conexao.cur.fetchone()
            
            procValores = None
            for produto in venda.produtosVenda:
                procValores = (produto.id, codVenda, produto.quantidade)
                conexao.execute('''INSERT INTO venda_produto(id_produto_produto, id_saida_venda, quantidade) 
                                    VALUES(%s,%s,%s)''', procValores)
                
            conexao.commit()
        except (Exception, conexao.psycopg2.DatabaseError) as error:
            conexao.rollback()
            print(error)
        finally:
            if conexao is not None:
                conexao.close()
                
    def retornaVendas(self):
        conexao = conexao.Connection()
        print('')
        conexao.query('SELECT * FROM venda')
        conexao.queryResult()
        conexao.close()
            
    def relatVendasPeriodo(self, dataInicial, dataFinal):
        conexao = conexao.Connection()
        params = (dataInicial, dataFinal)
        conexao.execute('''SELECT * FROM venda 
                            WHERE data_venda BETWEEN %s 
                            AND %s ''', params)
        conexao.queryResult()
        conexao.close()
    
    def relatVendasFuncionarioPeriodo(self, dataInicial, dataFinal, cpfFuncionario):
        conexao = conexao.Connection()
        params = (dataInicial, dataFinal, cpfFuncionario)
        conexao.execute('''SELECT * FROM venda 
                            WHERE data_venda BETWEEN %s 
                            AND %s 
                            AND cpf_funcionario_venda = %s''', params)
        conexao.queryResult()
        conexao.close()

    def relTotVendasFuncionarioPeriodo(self, dataInicial, dataFinal, cpfFuncionario):
        conexao = conexao.Connection()
        params = (dataInicial, dataFinal, cpfFuncionario)
        conexao.execute('''SELECT SUM(valor_total) AS TOTAL FROM venda 
                            WHERE data_venda BETWEEN %s 
                            AND %s 
                            AND cpf_funcionario_venda= %s
                            GROUP BY cpf_funcionario_venda''', params)
        conexao.queryResult()
        conexao.close()            