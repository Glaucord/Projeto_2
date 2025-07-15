# Projeto para mostrar o básico de operações matemáticas em python. 
print("Bem-vindo ao calculador de gorjeta!")

conta = float(input("Qual foi o valor da conta? R$"))

gorgeta = int(input("Qual porcentagem de gorjeta gostaria de dar? 10 12 15 "))

pessoas = int(input("Em quantas pessoas devemos separar a conta? "))

porcentagem_da_gorjeta = gorgeta / 100
conta_mais_gorjeta = conta * porcentagem_da_gorjeta
total_da_conta = conta + conta_mais_gorjeta
conta_por_pessoa = total_da_conta / pessoas
valor_total = round(conta_por_pessoa, 2)

print(f"Cada pessoa deverá pagar: R$ {valor_total}")
