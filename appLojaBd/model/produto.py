from model import connection as conexao
class Produto(object):
    '''
    classdocs
    '''


    def __init__(self, produto):
        '''
        Constructor
        '''
        self.produto = produto
    
    def procIADProduto(self, produto, operacao):
        procValores = (operacao, produto.id, produto.nome, 
                       produto.preco_venda, produto.preco_compra, produto.qtd_estoque)
        
        conexao = conexao.Connection()
        conexao.callProCedure(self, "insere_atualiza_deleta_produto" , procValores)
        conexao.close()
        
    def retornaProdutos(self):
        conexao = conexao.Connection()
        print('')
        conexao.query('SELECT * FROM produto')
        conexao.queryResult()
        conexao.close()
        
    def relatProdutosVendidos(self, params): 
        conexao = conexao.Connection()
        print('')
        conexao.execute('''SELECT vp.id_produto_produto, p.nome, sum(vp.quantidade) AS qtd_total
                            FROM venda_produto AS vp
                            INNER JOIN produto AS p ON ( p.id_produto = vp.id_produto_produto )
                            GROUP BY vp.id_produto_produto, p.nome
                            ORDER BY
                            qtd_total %s 
                            LIMIT %s ''', params)
        conexao.queryResult()
        conexao.close()      