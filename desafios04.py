#faca um programa que recebe o salario-base de um funcionario, calcule e mostre 
#o salario a receber, sabendo que este funcionario tem gratificacao de 5%
#sobre o salario-base e paga imposto de 7% sobre o salario-base 

salario_base = float(input("Digite seu salario-base "))

gratificacao = salario_base * 0.05
imposto = salario_base * 0.07
print(f"salario liquido: {salario_base + gratificacao - imposto:.2f} ")
