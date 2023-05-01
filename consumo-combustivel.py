if __name__ == "__main__":
    km = float(input("Qual foi a distância percorrida pelo automóvel?"))
    l = float(input("Qual a quantidade de combustível usada para percorrer essa distância?"))
    
    consumo = km / l

    print("O consumo médio de combustível desse automóvel é de {0:.2f}km/l".format(consumo))