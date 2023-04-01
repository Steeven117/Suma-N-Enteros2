# Suma de numeros con el while

N=int(input("Digite el valor de N: "))
i=1
Suma=0

while(i<=N):
    Suma = Suma + i
    i= i+1
    print("i="+str(i))
    print("Suma="+str(Suma))

print("La suma es: "+str(Suma))

