produtos = []
opcao = "0"
while opcao !="5":
    print(""" ======== CONTROLE DE ESTOQUE========
    1 - "Cadastrar produto"
    2 - "Listar produtos"
    3 - "Registrar entrada"
    4 - "Registrar saida"
    5 - "Sair"
    """)

    opcao = input("Escolha uma opção: ")
    if opcao =="1":
        print("Cadastre seu produto")
        nome=input("Digite o nome do produto: ").strip()
        if nome == "":
            print("O nome não pode ficar vazio!")
        else:
            encontrado = False
            for i in produtos:
                if nome.lower() == i["nome"].lower():
                    encontrado = True
            if encontrado:
                print("Produto já existe!")
            else:
                try:
                    preco=float(input("Digite o preço do produto: "))
                except ValueError:
                    print("Digite um preço válido")
                else:
                    if preco<=0:
                        print("Preço não pode ser registrado")
                    else:
                        try:
                            quantidade=int(input("Digite a quantidade do produto em estoque: "))
                        except ValueError:
                            print("Digite uma quantidade válida!")
                        else:
                            if quantidade<=0:
                                print("Quantidade não pode ser registrada")
                            else:
                                produto ={
                                        "nome": nome,
                                        "preco": preco,
                                        "quantidade": quantidade
                                    }
                                produtos.append(produto)
                                print("Produto cadastrado com sucesso!")
    elif opcao =="2":
        print("Lista de produtos cadastrado: ")
        if len(produtos)==0:
             print("Nenhum produto cadastrado!")
        else:
             print(f"Total de produtos cadastrados: {len(produtos)}")
             print()
             for produto in produtos:
                print(f"Nome:{produto ['nome']}")
                print(f"Preço: R$ {produto['preco']:.2f}")
                print(f"Quantidade: {produto ['quantidade']}")
                print()
    elif opcao =="3":
        print("Vamos registrar uma entrada ")
        nome = input("Digite o nome do produto: ")
        encontrado = False
        for produto in produtos:
            if nome.lower() == produto["nome"].lower():
                encontrado = True
                try:
                    entrada=int(input(" Quantas unidades chegaram?: "))
                except ValueError:
                    print("Digite uma quantidade válida!")
                else:
                    if entrada<=0:
                        print("Quantidade inválida!")
                    else:
                        produto['quantidade'] +=entrada
                        print("Entrada registrada com sucesso!")
                        print(f'Estoque atualizado: {produto["quantidade"]}')
        if not encontrado:
            print("produto não existe!")
    elif opcao =="4":
        print("Vamos registrar uma saida: ")
        nome=input("Digite o nome do produto: ").strip()
        encontrado = False
        for produto in produtos:
            if nome.lower() ==produto["nome"].lower():
                encontrado = True
                try:
                    entrada=int(input("Quantas unidades sairam?: "))
                except ValueError:
                    print("Digite uma quantidade válida")
                else:
                    if entrada<=0:
                        print("quantidade inválida!")
                    else:
                        if produto["quantidade"] >=entrada:
                            produto['quantidade'] -=entrada
                            print("Saida registrada com sucesso!")
                            print(f"Estoque atualizado!: {produto['quantidade']}")
                        else:
                            print("Estoque insuficiente!")
        if not encontrado:
            print("Produto não existe!")
    elif opcao =="5":
        print("Encerrando sistema...")
        break
    else:
        print("Opção invalida")
        




