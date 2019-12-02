from controller.validacoes import validaCpf, validaNome, validaEmail
from model.cliente import Cliente as ModelCliente

class Cliente(object):
    '''
    classDocs
    '''
    
    def __init__(self, cpf="", nome="", email="", rua="", numero="" ,bairro="", cidade=""):
        '''
        Constructor
        '''
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.mCliente = ModelCliente()
        
    def validaCliente(self):
        if validaCpf(self.cpf) == False:
            return False
        if validaNome(self.nome) == False:
            return False
        if validaEmail(self.email) == False:
            return False
    
    def dadosEdicaoCli(self, nome, email, rua, numero, bairro, cidade):
        if self.nome == "":
            self.nome = nome
        if self.email == "":
            self.email = email
        if self.rua == "":
            self.rua = rua
        if self.numero  == "":
            self.numero = numero
        if self.bairro == "":
            self.bairro = bairro
        if self.cidade == "":
            self.cidade = cidade
        
    def operacaoCliente(self, operacao):
        if operacao == "I":
            if self.validaCliente() == False:
                return False
        else:
            dadosCli = self.mCliente.recuperaDados(self.cpf)
            self.dadosEdicaoCli(*dadosCli)
            self.mCliente.procIADCliente(self, operacao)
    
    def listaClientes(self):
        self.mCliente.retornaClientes()