print("Insira números na forma decimal, apenas.")
print()
a1 = float(input ("Digite o primeito termo desejado: "))
n = int(input ("Insira o número de termos que há na progressão: "))
r = float(input ("Diga o valor da razão: "))

a = float(a1 * (r ** (n-1)))

print("O termo",n,"dessa progressão geométrica possui valor:",a)

s = (a1 * (((r**n)-1)/(r-1)))

print("A soma dos",n,"termos resulta em:",s)
