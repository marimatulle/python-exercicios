if __name__ == "__main__":
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))

    perimetro = 2 * (base + altura)
    area = base * altura

    print("A área do retângulo {0} * {1} = {2}".format(base, altura, area))
    print("O perímetro do retângulo {0} + {1} = {2}".format(base, altura, perimetro))