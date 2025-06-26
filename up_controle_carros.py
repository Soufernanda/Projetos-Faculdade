def calcular_media(anos):
    return sum(anos) / len(anos)  
#os dados dos carros:
def exibir_dados(carros):
    if not carros:  
        print("\nNenhum carro foi cadastrado.")
        return
    antigos = []
    menor_ano = float('inf')  
    soma = 0
    for carro in carros:
        marca, modelo, cor, ano = carro
        soma += ano
        if ano < menor_ano:
            menor_ano = ano
            antigos = [carro]  
        elif ano == menor_ano:
            antigos.append(carro)  

    media_ano = calcular_media([carro[3] for carro in carros]) 
    anos_unicos = set(carro[3] for carro in carros)
    if len(anos_unicos) == 1:
        print(f"\nTodos as marcas e modelos pertencem ao mesmo ano de fabricação: {menor_ano}")
    else:
        print("\nCarro(s) mais antigo(s):")
        for carro in antigos:
            print(f"Marca: {carro[0]}, Modelo: {carro[1]}, Cor: {carro[2]}, Ano: {carro[3]}")

    print(f"Média de ano de fabricação dos carros cadastrados: {media_ano:.2f}")

    print("\nLista de carros cadastrados:")
    for carro in carros:
        print(f"Marca: {carro[0]}, Modelo: {carro[1]}, Cor: {carro[2]}, Ano: {carro[3]}")

#Entrada:
carros = []
while True:
    marca = input("Marca do carro: ")
    modelo = input("Modelo do carro: ")
    cor = input("Cor do carro: ")  
    ano = int(input("Ano de fabricação do carro: "))
    carros.append((marca, modelo, cor, ano))  


    continuar = input("Deseja adicionar mais um carro? (s/n): ").strip().lower()
    if continuar != 's':
        break  


exibir_dados(carros)


