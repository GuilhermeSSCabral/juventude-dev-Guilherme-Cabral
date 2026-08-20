import random
print("=========================")
print("Desafio de calculo rápido")
print("=========================")
print("Escolha a dificuldade: ")
print("[1] Fácil")
print("[2] intermediário")
print("[3] Médio")
print("[4] Difícil")
print("[5] Impossível")
print("=========================")
dificuldade = int(input("Escolha: "))
print("=========================")

if dificuldade == 1:
    a = random.randint(1, 5)
    b = random.randint(3, 5)
    c = random.randint(2, 5)
    
    q1 = a + a + a
    q2 = a + b + b
    q3 = b + c + c
    q4 = int(a + b + c)
    
    print("a + a + a =", q1)
    print("a + b + b =", q2)
    print("b + c + c =", q3)
    print("a + b + c = ?")
    r = int(input("Resposta: "))
    
    if r == q4:
        print("Resposta Correta!")
    else:
        print("Resposta Incorreta ;(")


if dificuldade == 2:
    a = random.randint(5, 15)
    b = random.randint(3, 8)
    c = random.randint(4, 6)
    
    q1 = a + a + a
    q2 = a + b + b
    q3 = b + c + c
    q4 = int(a + b * c)
    
    print("a + a + a =", q1)
    print("a + b + b =", q2)
    print("b + c + c =", q3)
    print("a + b x c = ?")
    r = int(input("Resposta: "))
    
    if r == q4:
        print("Resposta Correta!")
    else:
        print("Resposta Incorreta ;(")


if dificuldade == 3:
    a = random.randint(5, 15)
    b = random.randint(3, 8)
    c = random.randint(4, 6)
    
    q1 = a + a + a
    q2 = a + b + b
    q3 = b + c + c
    q4 = float(a * b / c)
    
    print("a + a + a =", q1)
    print("a + b + b =", q2)
    print("b + c + c =", q3)
    print("a x b / c = ?")
    r = float(input("Resposta: "))
    
    if r == q4:
        print("Resposta Correta!")
    else:
        print("Resposta Incorreta ;(")


if dificuldade == 4:
    a = random.randint(10, 15)
    b = random.randint(7, 12)
    c = random.randint(8, 9)
    
    q1 = a + a * a
    q2 = a * b + b
    q3 = b + c + c
    q4 = int(a + b + c)
    
    print("a + a x a =", q1)
    print("a x b + b =", q2)
    print("b + c + c =", q3)
    print("a + b + c = ?")
    r = int(input("Resposta: "))
    
    if r == q4:
        print("Resposta Correta!")
    else:
        print("Resposta Incorreta ;(")
        

if dificuldade == 5:
    a = random.randint(10, 50)
    b = random.randint(8, 11)
    c = random.randint(1, 3)
    
    q1 = a + a + a
    q2 = a + b + b
    q3 = b + c + c
    q4 = a + (b ** c)
    
    print("a + a + a =", q1)
    print("a + b + b =", q2)
    print("b + c + c =", q3)
    print("a + b ** c = ?")
    r = int(input("Resposta: "))
    
    if r == q4:
        print("Resposta Correta!")
    else:
        print("Resposta Incorreta ;(")



