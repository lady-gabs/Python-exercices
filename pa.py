a1 = float(input ("Digite o primeiro termo desejado: "))
n = int(input("Insira o número de termos que há na progressão: "))
r= float(input("Diga qual o valor da razão: "))

x= a1 + (n-1) * r
an = float(x)

print("O termo",n,"dessa progressão aritmética possui valor:",an)


sn=((a1+an)*n)/2

print("A soma dos",n, "termos será:",sn)
