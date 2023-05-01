def combustivel(quantidade,valor):
    if(quantidade<=20):
        return((quantidade*valor)+(valor*0.03))
    elif(quantidade>20 and quantidade<=40):
        return((quantidade*valor)+(valor*0.05))
    else:
        print("O desconto não se aplica a quantidade abastecida")

if __name__ == "__main__":
    quantidade = float(input("Quantos litros você irá abastecer? "))
    valor = float(input("Qual o preço do litro? "))
    
    resultado = combustivel(quantidade,valor)

    print("O valor será de {} reais".format(resultado))