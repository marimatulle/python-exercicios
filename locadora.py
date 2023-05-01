if __name__ == "__main__":
    fitas = int(input("Quantas fitas existem na locadora?"))
    aluguel = float(input("Qual o valor do aluguel das fitas?"))

    faturamento_anual = (fitas / 3) * 12
    juros_atraso = ((fitas / 10) * 0.10) * (fitas / 3)
    
    print("A locadora fatura anualmente R${0:.2f} e ganha com juros das fitas atrasadas R${1:.2f}".format(faturamento_anual,juros_atraso))
