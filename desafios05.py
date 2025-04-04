#faca um programa que recebe o salario-base de um funcionario, calcule e mostre 
#o salario a receber, sabendo que este funcionario tem uma gratificacao de 
#R$50,00 e paga um imposto de 10% sobre o salario-base 

salario_base = float(input("Digite seu salario-base "))

imposto = salario_base * 0.1
print(f"salario liquido: {salario_base + 50 - imposto:.2f} ")
