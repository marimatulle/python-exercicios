def idade(a,m,d):
    return(d + (a * 360) + (m * 30))

if __name__ == "__main__":
    x = int(input("Digite seu ano de nascimento: "))
    y = int(input("Digite seu mês de nascimento: "))
    z = int(input("Digite seu dia de nascimento: "))

    dias_idade = idade(x,y,z)
    
    print("Contando com todos os meses tendo 30 dias, você viveu {} dias".format(dias_idade))
