#lendo um numero do teclado 
aux = input("digite um numero")
#convertendo a informaçao para int
num_a = int(aux)

aux = input("digite o segundo numero")
num_b = int(aux)

#processamento 
prod = num_a * num_b 
soma = num_a + num_b
div = num_a // num_b
rest = num_a % num_b 

print("soma", soma)
print("multiplicacao", prod)
print("divisao", div)
print("resto", rest)