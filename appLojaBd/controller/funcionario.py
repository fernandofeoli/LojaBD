from model.funcionario import Funcionario as modelFuncionario
from controller.validacoes import validaCpf, validaNome, validaEmail

class Funcionario(object):
    '''
    classdocs
    '''


    def __init__(self, cpf="", nome="", email="", senha="", flagGerente="" ):
        '''
        Constructor
        '''
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.senha = senha
        self.flagGerente = flagGerente
        self.mFuncionario = modelFuncionario()
        
    def validaFuncionario(self):
        if validaCpf(self.cpf) == False:
            return False
        elif validaNome(self.nome) == False:
            return False
        elif validaEmail(self.email) == False:
            return False
        elif self.validaSenha(self.senha) == False:
            return False
        
    def validaCargo(self):
        return self.mFuncionario.verificaGerente(self.cpf)
         
    def validaSenha(self):
        if (self.senha == ""):
            print("Senha em branco!")
            return False
        elif (len(self.senha) > 50):
            print("Senha possui mais de 50 caracteres!")
            return False
            
    def operacaoFuncionario(self, operacao):
        self.mFuncionario.procIADFuncionario(self, operacao)

    def listaFuncionarios(self):
        self.mFuncionario.retornaFuncionarios()