n1 = int(input("Type a number/ Digite um numero "))
n2 = int(input("Type a a second number/ Digite um segundo numero "))
calcular = input("Selecione uma opeação \n a - adção \n s - subtração \n m - multiplicação \n d - divisão \n")

a = ("a")
s = ("s")
m = ("m")
d = ("d")

if calcular == a:
    print(n1 + n2)

elif calcular == s:
    print(n1 - n2)

elif calcular == m:
    print(n1 * n2)

elif calcular == d:
    print(n1 // n2)

else:
    print("Digite \n a=adição \n s=subtração \n m=multiplicar \n d=divisão \n na proxima vez")
