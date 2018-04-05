print("Salario mais comissão")
#entrada de dados
salario = float(input("digite o valor do salario R$: "))
valor_vendas = float(input("digite o valor das vendas R$: "))
#calculo de salario + comissão de 4%
salario_comissao = (salario +(valor_vendas * 0.04))
#saida
print("O valor do sálario com valor da comissão é R$: {:06.2f}".format(salario_comissao))