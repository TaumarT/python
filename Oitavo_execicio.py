print("Calculo de Horas trabalhadas")
valor = float(input("digite quanto vc ganha por hora: "))
horas = int(input("digite quantas horas trabalhadas no mês: "))

salario = (valor * horas)
print("Você ganha R$:{:06.2f}".format(salario))