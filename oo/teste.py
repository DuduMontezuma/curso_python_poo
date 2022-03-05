

def cria_conta(numero, titular, saldo, limite):
    conta = {"número": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def depositar(conta, valor):
    conta["saldo"] += valor

def sacar(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print(f"saldo: {conta['saldo']}")