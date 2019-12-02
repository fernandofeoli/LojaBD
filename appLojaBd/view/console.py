from controller.sessao import setUsuario
from controller.cliente import Cliente 
import getpass

def menuLogin():
    while not False:
        email = input("Email: ")
        senha = getpass.getpass(prompt='Senha: ', stream=None) 
        usuario = setUsuario(email, senha)
        if usuario != False:
            return usuario
        
def edtIstDelCliente(op):
    nome = ""
    email = ""
    rua = "" 
    numero = ""
    bairro = "" 
    cidade = ""
    cpf = input("CPF: ")
    if op == "A" or op == "I":
        nome = input("Nome: ")
        email = input("E-Mail: ")
        rua = input("Rua: ") 
        numero = input("Numero: ")
        bairro = input("Bairro: ") 
        cidade = input("Cidade: ")
    cli = Cliente(cpf, nome, email, rua, numero, bairro, cidade)
    cli.operacaoCliente(op)   
    
def menuclientes():
    while not False:
        print('''
                 1 - Listar clientes
                 2 - Cadastrar Clientes''')
        op = input("Opção: ")
        if op != "1" and op != "2":
            print("Opção inválida!")
        elif op == "1":
            cli = Cliente()
            cli.listaClientes()
            print('''
                     1 - Editar cliente
                     2 - Excluir Cliente''')
            op = input("Opção: ")
            if op != "1" and op != "2":
                print("Opção inválida!")    
            elif op == "1":
                print("Os Valores que não deseja editar, deixe vazio!")
                edtIstDelCliente("A")
            elif op == "2":
                edtIstDelCliente("D")
        elif op == "2":
            edtIstDelCliente("I")

 
print("Bem vindo ao Akatsuki Vendas.")
print("Por favor, efetue o login.")

''' Descomentar Após testes!
usuario = menuLogin()
print("Olá",usuario.nome,"Selecione a opção desejada: ") 
'''

print('''
         1 - Clientes
         2 - Fornecedores
         3 - Funcionarios
         4 - Produtos
         5 - Compras
         6 - Vendas''')
opcao = input("Opção: ")

if opcao == "1":
    menuclientes()

