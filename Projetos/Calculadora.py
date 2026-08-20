print("Bem-Vindo!")
print("==============")
print("[1] Soma")
print("[2] Subtração")
print("[3] Multiplicação")
print("[4] Divisão")
print("[5] Regra de 3")
print("[6] Báskara")
print("[7] IMC")
print("==============")
opcao = input("qual operação vc quer:")
print("==============")

if opcao == "1":
    a = float(input("digite o primeiro valor:"))
    b = float(input("digite o segundo valor:"))
    
    c = a + b
    print("A soma entre é de", c)

if opcao == "2":
    a = float(input("digite o primeiro valor:"))
    b = float(input("digite o segundo valor:"))
    
    c = a - b
    print("A subtração entre é de", c)

if opcao == "3":
    a = float(input("digite o primeiro valor:"))
    b = float(input("digite o segundo valor:"))
    (input("digite o segundo valor:"))
    
    c = a * b
    print("A Multiplicação é de", c)

if opcao == "4":
    a = float(input("digite o primeiro valor:"))
    b = float(input("digite o segundo valor:"))
    
    c = a / b
    print("A Divisão entre é de", c)

if opcao == "5":
    print("escreva no formato de:")
    print("a   b")
    print("c   X")
    print("-----------------------")
    a = input("digite o valor de A: ")
    b = input("digite o valor de B: ")
    c = input("digite o valor de C: ")

    print("-----------------------")
    pro_inv = input("Ela e proporcional? (Sim ou Não): ")

    a_value = int(a)
    b_value = int(b)
    c_value = int(c)

    if pro_inv == "Sim":
        x = (c_value * b_value) / (a_value)
    else:
        x = (a_value * b_value) / (c_value)
    print("-----------------------")
    print("O valor de x é igual a: ",  x)

if opcao == "6":
    import math
    
    a = input("Digite o valor de a: ")
    b = input("Digite o valor de b: ")
    c = input("Digite o valor de c: ")
    
    a_value = int(a)
    b_value = int(b)
    c_value = int(c)
    
    delta = (b_value ** 2) - (4 * a_value * c_value)
    
    if delta <0:
        print("----------------------------")
        print("esse número não possiu raiz exata.")
    else:
        b1 = (- b_value + math.sqrt(delta)) / (2 * a_value)
    
        b2 = (- b_value - math.sqrt(delta)) / (2 * a_value)
    
        print("----------------------------")
        print("O primeiro valor é: ", b1)
        print("O Segundo valor é: ", b2)

        
if opcao == "7":
    peso = int(input("Qual o seu peso(KG): "))
    altura = float(input("Qaul a sua altura(m): "))
    
    imc = (peso) / (altura ** 2)
    
    print ("seu IMC é de:", imc)
    
    if imc < 18.5:
        print("Você está abaixo do peso.")
        
    elif imc <= 24.9:
        print("Você está no peso ideal.")
        
    elif imc <= 29.9:
        print("Você está levemente acima do peso.")
        
    elif imc <= 34.9:
        print("Você está com obesidade Grau 1.")
        
    elif imc <= 39.9:
        print("Você está com obesidade Grau 2(Severa).")
        
    elif imc >= 40:
        print("Você está com obesidade Grau 3(Mórbida).")


else:
    print(opcao, ", não é uma opção disponivel.")
