import controller.funcionario as func
import controller.vendedor as vend
from model.gerente import  Gerente as modelGerente

class Gerente(func.Funcionario):
    '''
    classdocs
    '''


    def __init__(self, cpf="", nome="", email="", senha="", flagGerente=True):
        super().__init__(cpf, nome, email, senha, flagGerente)
        '''
        Constructor
        '''
        self.mGerente = modelGerente()
    def novoGerente(self, cpfGerente, operacao):
        if self.validaCargo(cpfGerente) == True:
            self.validaFuncionario(self.cpf, self.nome, self.email, self.senha)
            self.procIADFuncionario(self, operacao)
        else:
            print("Você não tem permissão para efetuar essa operação!")
            return False
            
    def criarFuncionario(self, cpf, nome, email, senha, flagGerente, operacao, cpfGerente=""):
        if flagGerente == True:
            gerente = Gerente(cpf, nome, email, senha, flagGerente)
            gerente.novoGerente(self.cpf, operacao)
        else:
            vendedor = vend.Vendedor(cpf, nome, email, senha, flagGerente, cpfGerente)
            vendedor.novoVendedor(self.cpf, operacao)
    
    def listaGerentes(self):
        self.mGerente.retornaGerentes()
        
    def listaSupervisionados(self):
        self.mGerente.verificaSupervisionados()