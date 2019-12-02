from model import connection as conexao

class Gerente(object):
    '''
    classdocs
    '''


    def __init__(self, gerente):
        '''
        Constructor
        '''
        self.gerente = gerente
    
    def verificaSupervisionados(self):
        param =()
        conexao = conexao.Connection()
        conexao.callProCedure(self, "verifica_supervisionados" , param)
        conexao.getqueryResult()
        conexao.close()
        
    def retornaGerentes(self):
        conexao = conexao.Connection()
        print('')
        conexao.query('SELECT * FROM gerente')
        conexao.queryResult()
        conexao.close()    