print("Desconto de produto")
produto = float(input("digite o valor do produto R$: "))

desconto = (produto -(produto * 0.10))

print("O valor do produto com desconto é R$: {:06.2f}".format( desconto))