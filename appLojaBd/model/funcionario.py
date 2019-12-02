from model import connection as conexao
class Funcionario(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def procIADFuncionario(self, funcionario, operacao):
        procValores = (operacao, funcionario.cpf, funcionario.nome, 
                       funcionario.email, funcionario.senha, funcionario.flagGerente)
        
        conexao = conexao.Connection()
        conexao.callProCedure(self, "insere_atualiza_deleta_funcionario" , procValores)
        conexao.close()
        
    def verificaGerente(self, cpf):
        conexao = conexao.Connection()
        conexao.execute('SELECT flagGerente FROM funcionario WHERE cpf = %s', (cpf))
        ret = conexao.cur.fetchone()
        conexao.close()
        return ret
    
    def verificaFuncionario(self, cpf):
        conexao = conexao.Connection()
        conexao.execute('SELECT cpf FROM funcionario WHERE cpf = %s', (cpf))
        ret = conexao.cur.fetchone()
        conexao.close()
        return ret
    
    def retornaFuncionarios(self):
        conexao = conexao.Connection()
        print('')
        conexao.query('SELECT * FROM funcionario')
        conexao.queryResult()
        conexao.close()
        