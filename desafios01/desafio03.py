#faca um programa que receba o salario de um funcionario e o percentual de 
#aumento, calcule  mostre o valor do aumento e do novo salario.


salario = float(input("salario do funcionario: "))
porcentagem = float(input("percentual de aumento :"))
aumento = (porcentagem / 100) * salario100010
#novo_salario = salario + aumento
print(f" o salario novo é de R${salario + aumento:.2f}") 
