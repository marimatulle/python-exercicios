if __name__ == "__main__":
    valor = float(input("Digite o valor do produto: "))
    taxa = float(input("Digite a taxa de juros: "))
    tempo = int(input("Digite os dias de atraso: "))

    atraso = valor + (valor * (taxa / 100) * tempo)
    
    print("O valor dos juros da sua prestação é de {0:.2f} reais".format(atraso))