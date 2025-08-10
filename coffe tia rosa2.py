################################# COFFE SHOPS TIA ROSA #####################################################################################################


#começo fazendo as nossas opções em forma de dicionário que nesse caso serão 3:estoque, proços e promoções.
#faço duas listas com as varíaveis clientes e vendas diarias.


estoque = {"Cafézinho": 55,"Pingado" : 52,"Biscoito de queijo": 23,"Pão de queijo" : 41,"Bolo de cenoura":26}

precos = {"Cafézinho":1.50,"pingado": 3.00, "Biscoito de queijo": 5.00, "Pão de queijo":2.50,"Bolo de cenoura":5.25}

promocoes = { ("Cafézinho", "Pão de queijo"):3.00, ("Biscoito de queijo", "pingado"): 6.50}


clientes = []
vendas_diarias = []


#agora definimos as funções que esse código vai ter.


def Cardápio ():
    print ("\n Cardápio")
    for item, preco in precos.items():
        print (f"{item} - R$ {preco:.2f}", end = "")
        if item in promocoes:
            print(f" promoção: {promocoes[item]}")
        else:
            print()

#tive dificuldade nessa função porque não peguei o jeito direito ainda de colocar as casas decimais


def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    celular = input("Digite o número de celular: ")
    email = input("Digite o email desejado: ")
    endereco = input("Digite o endereço: ")
    clientes.append({nome:"nome", celular:"celular", email:"email", endereco:"endereço"})
    print(f":cliente {nome}, cadastrado com sucesso!")
    
 #essa funçao é mais tranquila só pedir os dasdos cadastrais do cliente, e depos colocar o "append" pra adicionar o cliente na variavel "Cliente"

def fazer_pedido():
    Cardápio() 
    pedido =  input ("Digite o nome do item: ")
        
    if pedido not in estoque:
        print("Este item não está no cardápio")
        return

    try:
        quantidade = int(input("Quantidade: "))

    except ValueError:
        print("Quantidade inválida. ")
        return
    if quantidade > estoque [ pedido ] :
        print ("Estoque insuficiente")
        return
    
   

    estoque[pedido] -= quantidade
    valor_total = precos[pedido] * quantidade
    vendas_diarias.append(valor_total)

#A função fazer pedido está pronta, juntamente com os if's caso o produto escolhido não estiver no cardápio ou se a quantidade pedida for superior a que temos no estoque.

def Consultar_estoque():
    print ("\n Estoque ")
    for item, qtd in estoque.items():
        print(f"{item}: {qtd} unidades ")

#Aqui o estoque está definido

def calcular_vendas_do_dia():
    total = sum (vendas_diarias)
    print(f"Venda diária: R$ {total:.2f}")

#Agora fazemos essa funçao para o calculo das vendas da cafeteria por dia.

def pagina_inicial():
    while True:
        print("\n Bem vindo ao Coffe Shops Tia Rosa!")
        print("1. Cardápio")
        print("2. Cadastrar novo cliente")
        print("3. Fazer pedido")
        print("4. Consultar estoque")
        print("5. Calcular venda diária")
        print("6. Fechar")

        opcao = input("Escolha uma opção: ")

        if opcao == '1': 
            Cardápio()
        elif opcao == '2':
            cadastrar_cliente()
        elif opcao == '3':
            fazer_pedido()
        elif opcao == '4':
            Consultar_estoque()
        elif opcao == '5':
            calcular_vendas_do_dia()
        elif opcao == '6':
            print('O sistema será fechado, o Coffe Shops Tia Rosa agradece sua presença')
        
        else:
            print (" Opção Inválida ")
        
#Aqui utilizo as funções if,elif e else para organizar nossa página inicial do sistema e dando as opções disponíveis.



#Com a estrutura do código pronta podemos executar o programa.
pagina_inicial()         

    
    
           
