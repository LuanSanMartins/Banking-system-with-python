import textwrap

# ==================================================================================================================== 
# ===== Este projeto foi elaborado pelo professor Guilerme Carvalho e editado por Luan Carlos Martins dos Santos ===== #
# ==================================================================================================================== #

width = 100

def menu():
    print("\n")
    print(" MENU ".center(width, "="))
    menu = """
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo = saldo + valor
        extrato = extrato + f"Depósito:\tR$ {valor:.2f}\n"
        print(" Depósito realizado com sucesso! ".center(width, "="))
        
    else:
        print("\n")
        print(" Operação falhou! O valor informado é inválido. ".center(width, "@"))

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n")
        print(" Operação falhou! Você não tem saldo suficiente. ".center(width, "@"))

    elif excedeu_limite:
        print("\n")
        print(" Operação falhou! O valor do saque excede o limite. ".center(width, "@"))

    elif excedeu_saques:
        print("\n")
        print(" Operação falhou! Número máximo de saques excedido. ".center(width, "@"))

    elif valor > 0:
        saldo = saldo - valor
        extrato = extrato + f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques = numero_saques + 1
        print("\n")
        print(" Saque realizado com sucesso! ".center(width, "="))

    else:
        print("\n")
        print(" Operação falhou! O valor informado é inválido. ".center(width, "@"))

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print(" EXTRATO ".center(width, "="))
    #print("Não foram realizadas movimentações." if not extrato else extrato)
    if not extrato:
        print("\n")
        print("Não foram realizadas movimentações.")
    else:
        print("\n")
        print(extrato)

    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("".center(width, "="))

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n")
        print(" Já existe usuário com esse CPF! ".center(width, "@"))
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n")
    print(" Usuário criado com sucesso! ".center(width, "="))

def filtrar_usuario(cpf, usuarios):
    # usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    # return usuarios_filtrados[0] if usuarios_filtrados else None

    usuarios_filtrados = []
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuarios_filtrados.append(usuario)

    if usuarios_filtrados:
        return usuarios_filtrados[0]

    else:
        return None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n")
        print(" Conta criada com sucesso! ".center(width, "="))
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n")
    print(" Usuário não encontrado, fluxo de criação de conta encerrado! ".center(width, "@"))

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\n")
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
