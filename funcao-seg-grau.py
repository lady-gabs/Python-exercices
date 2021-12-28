import math

print("Dada a função: a * (x^2) + b * x + c = 0")
print ()
a = float (input("Insira o coeficiente angular (a): "))
b = float (input("Insira o coeficiente linear (b): "))
c = float (input("Insira o termo independente (c): "))

i = complex (0,1)
d = ((b ** 2) - (4 * a * c))

if (d)> 0:
    delta = math.sqrt(d)
    x1 = (- b + delta) / (2 * a)
    x2 = (- b - delta) / (2 * a)
    print ("As raízes da função são:", x1, "e", x2)
elif (d)==0:
    x = (-b) / (2 * a)
    print ("A raíz da função é:", x)
elif (d)<0:
    print ("Não há raízes reais para esta função, mas sim raízes complexas")
