from math import sqrt
print("Valor da hipotenusa")

pri_cateto = int(input("digito o valor do primeiro cateto: "))
seg_cateto = int(input("digito o valor do segundo cateto: "))

hipotenusa = ((pri_cateto ** 2) + (seg_cateto ** 2))

hip_raiz = sqrt(hipotenusa)

print("o valor da hipotenuza é :",int(hip_raiz))