import random
continuar  = "S"
Perro = 0 
Pcerto = 0

while continuar.upper () == "S" :
    ns = random.randint(1,10)

    T = 3

    while( T > 0):
        print(" voce tem" , T, "tentativa")
        T = T -1

        nc = int(input ("Digite um Número de 1 a 10: "))
        if (ns == nc):
            print("você acertou.")
            T = 0
            Pcerto = Pcerto + 1 
        else:
            print("você errou.")
            Perro = Perro + 1
        print("numero de acerto:", Pcerto)
        print("numero  de erros:", Perro)


continuar = input("deseja continuar (S)im")
