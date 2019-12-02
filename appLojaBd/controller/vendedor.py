import controller.funcionario as func
from model.vendedor import Vendedor as modelVendedor

class Vendedor(func.Funcionario):
    '''
    classdocs
    '''


    def __init__(self, cpf, nome, email, senha, flagGerente, meta, cpfGerente):
        super().__init__(cpf="", nome="", email="", senha="", flagGerente=False)
        '''
        Constructor
        '''
        self.meta = 0
        self.mVendedor = modelVendedor()
        self.cpfGerente = cpfGerente
        
    def validaMeta(self):
        if self.meta.isdigit() == False:
            print("Meta só pode conter numeros!")
            return False
        if (self.meta == 0):
            print("Informe uma meta para o vendedor!")
            return False

    def validaCpfGerente(self):
        if self.cpfGerente == "":
            print("CPF do gerente em branco!")
            return False
        elif self.cpfGerente.isdigit() == False:
            print("CPF do gerente só pode conter numeros!")
            return False
        elif len(self.cpfGerente) > 11:
            print("CPF do gerente possui mais de 11 digitos!")
            return False

    def validaVendedor(self):
        self.validaFuncionario(self.cpf, self.nome, self.email, self.senha)
        self.validaMeta(self.meta)
        self.validaCpfGerente(self.cpfGerente)
            
    def novoVendedor(self, cpfGerente, operacao):
        if self.validaCargo(cpfGerente) == True:
            self.validaVendedor()
            self.procIADFuncionario(self, operacao)
        else:
            print("Você não tem permissão para efetuar essa operação!")
            return False
    
    def verificaMeta(self,mes,ano):
        parametros = (self.cpf, mes, ano)
        print(self.mVendedor.verificaMeta(parametros))
        
    def verificaSupervisor(self):
        print(self.mVendedor.verificaSupervisor(self.cpf))
        
    def listaVendedores(self):
        self.mVendedor.retornaVendedores()