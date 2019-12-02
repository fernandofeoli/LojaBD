from model import sessao as session
from controller import funcionario as func

def setUsuario(email, senha):
    
    usuario = session.checaUsuário(email, senha)
    if usuario == None:
        print("Email ou senha incorreto!")
        return False
    else:
        funcionario = func.Funcionario(*usuario)
        return funcionario