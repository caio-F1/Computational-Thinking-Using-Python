#faca um programa que receba o valor de um deposito e o valor da taxa de juros, 
#calcule e mostre o valor do rendimnto e o valor total apos o rendimento 

deposito = float(input("Digite o seu deposito: "))
juros = int(input("taxa de juros: "))

rendimento = deposito * (juros / 100)

print(f"rendimento: {rendimento}")
print(f"Valor total: {deposito + rendimento}")
