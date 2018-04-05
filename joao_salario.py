print("calculos para joao")

salario = float(input("digite seu salario: "))
valor_contas = float(input("digite valor das contas juntas: "))

multa = valor_contas + (valor_contas * 0.02)

salario = float(salario - multa)

print("O valor que irá sobrar dos eu salario é de R$:{:06.2f}".format(salario))