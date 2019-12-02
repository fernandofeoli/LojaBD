from datetime import datetime
from model.fornecedor import Fornecedor as modelFornecedor
from model.compra import Compra as modelCompra

class Compra(object):
    '''
    classdocs
    '''


    def __init__(self, cnpjFornecedor):
        '''
        Constructor
        '''
        self.idEntrada = 0
        self.cnpjFornecedor = cnpjFornecedor
        self.dataCompra = datetime.now()
        self.valorTotal = 0
        self.produtosCompra = []
        self.mFornecedor = modelFornecedor()
        self.mCompra = modelCompra()
    
    def addProduto(self, produto):
        self.produtosCompra.append(produto)
    
    def delProduto(self, numProduto):
        try:
            del(self.produtosCompra[numProduto])
        except IndexError:
            print("Este produto não existe na lista de produtos!")
        
    def iniciaCompra(self):
        ret = self.mFornecedor.VerificaFornecedor(self.cnpjFornecedor)
        if ret == "":
            print("Fornecedor não encontrado!")
            return False
    
    def fechaCompra(self):
        pass
    
    def listaCompras(self):
        self.mCompra.retornaCompras()
        
    def relatoriosCompras(self, op, parametros):
        if op == 1:
            self.mCompra.relatComprasPeriodo(*parametros)
        elif op == 2:
            self.mCompra.relatComprasFornecedorPeriodo(*parametros)
        else:
            print("Operação inválida!")
        
        