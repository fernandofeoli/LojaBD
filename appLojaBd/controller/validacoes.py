'''
Arquivo de validações genéricas para os demais objetos
'''

def validaNome(nome):
    nome = nome.strip()
    if nome == "":
        print("Nome em branco!")
        return False
    elif nome.isalpha() == False:
        print("Nome só pode conter letras!")
        return False  
    elif len(nome) > 20:
        print("Nome possui mais de 20 caracteres!")
        return False
        
def validaEmail(email):
    if email == "":
        print("E-Mail em branco!")
        return False
    elif len(email) > 30:
        print("E-Mail possui mais de 30 caracteres!")
        return False
    
def validaCpf(cpf):
    if cpf == "":
        print("CPF em branco!")
        return False
    elif cpf.isdigit() == False:
        print("CPF só pode conter numeros!")
        return False
    elif len(cpf) > 11:
        print("CPF possui mais de 11 digitos!")
        return False
        
def validaCnpj(cnpj):
    if cnpj == "":
        print("CNPJ em branco!")
        return False
    elif cnpj.isdigit() == False:
        print("CNPJ só pode conter numeros!")
        return False
    elif len(cnpj) > 14:
        print("CNPJ possui mais de 14 digitos!")
        return False