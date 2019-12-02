from model import connection as conex
import pandas as pd
from tabulate import tabulate
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

class Cliente(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def procIADCliente(self, cliente, operacao):
        procValores = (operacao, cliente.cpf, cliente.nome, 
                       cliente.email, cliente.rua, cliente.numero,
                       cliente.bairro, cliente.cidade)
        
        conexao = conex.Connection()
        conexao.callProCedure("insere_atualiza_deleta_cliente" , procValores)
        conexao.commit()
        conexao.close()
        
    def recuperaDados(self, cpf):
        param = (cpf,)
        conexao = conex.Connection()
        conexao.execute( '''SELECT nome_cliente, email_cliente, rua_cliente, numero_cliente,
                            bairro_cliente, cidade_cliente 
                            FROM cliente WHERE cpf = %s ''' , param)
        ret = conexao.cur.fetchone()
        conexao.close()
        return ret
        
    def retornaClientes(self):
        conexao = conex.Connection()
        data = pd.read_sql('SELECT * FROM cliente', conexao.conn)
        data = data.rename({"cpf":"CPF","nome_cliente":"Nome",
                            "email_cliente":"E-Mail","rua_cliente":"Rua",
                            "numero_cliente":"Numero","bairro_cliente":"Bairro",
                            "cidade_cliente":"Cidade"}, axis='columns')
        
        print("")
        print(tabulate(data, showindex=False, headers=data.columns, numalign="left"))
        conexao.close()