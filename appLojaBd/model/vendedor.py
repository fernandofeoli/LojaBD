from model import connection as conexao

class Vendedor(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def verificaMeta(self, procValores):
        conexao = conexao.Connection()
        conexao.callProCedure(self, "verifica_meta_vendedor" , procValores)
        ret = conexao.cur.fetchone()
        conexao.close()
        return ret
    
    def verificaSupervisor(self, cpfVendedor):
        conexao = conexao.Connection()
        conexao.callProCedure(self, "verifica_supervisor" , cpfVendedor)
        ret = conexao.cur.fetchone()
        conexao.close()
        return ret
    
    def retornaVendedores(self):
        conexao = conexao.Connection()
        print('')
        conexao.query('SELECT * FROM vendedor')
        conexao.queryResult()
        conexao.close()