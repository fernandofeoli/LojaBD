from datetime import datetime
from model.funcionario import Funcionario as modelFuncionario
from model.cliente import Cliente as modelCliente
from model.venda import Venda as modelVenda

class Venda(object):
    '''
    classdocs
    '''


    def __init__(self, cpfFuncionario, cpfCliente):
        '''
        Constructor
        '''
        self.idSaida = 0
        self.cpfFuncionario = cpfFuncionario
        self.cpfCliente = cpfCliente
        self.dataVenda = datetime.now()
        self.valorTotal = 0
        self.produtosVenda = []
        self.mCliente = modelCliente()
        self.mFuncionario = modelFuncionario()
        self.mVenda = modelVenda() 
           
    def addProduto(self, produto):
        self.produtosVenda.append(produto)
    
    def delProduto(self, numProduto):
        try:
            del(self.produtosVenda[numProduto])
        except IndexError:
            print("Este produto não existe na lista de produtos!")
            return False
        
    def iniciaVenda(self):
        ret = self.mFuncionario.verificaFuncionario(self.cpfFuncionario)
        if ret == "":
            print("Funcionario não encontrado!")
            return False
        ret = self.mCliente.VerificaCliente(self.cpfCliente)
        if ret == "":
            print("Cliente não encontrado!")
            return False
    
    def fechaVenda(self):
        pass
    
    def listaVendas(self):
        self.mVenda.retornaVendas()
          
    def relatoriosVendas(self, op, parametros):
        if op == 1:
            self.mVenda.relatVendasPeriodo(*parametros)
        elif op == 2:
            self.mVenda.relatVendasFuncionarioPeriodo(*parametros)
        else:
            print("Operação inválida!")
            return False
    