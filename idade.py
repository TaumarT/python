print("Calculo de idade")

ano_nascimento = int(input("Digite o ano que nasceu: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano_nascimento
idade_mes = idade * 12
idade_dias = idade * 365
idade_semana = idade * 52


print("Sua idade é:",idade )
print("Sua idade em meses é:",idade_mes)
print("Sua idade em dias é:",idade_dias)
print("Sua idade em semanas é:",idade_semana)




