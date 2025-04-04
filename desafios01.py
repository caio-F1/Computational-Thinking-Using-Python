#faca um progama que receba tresnotas e seus respectivos pesos, calcule e mostre a media ponderada dessas notas 

n1 = float(input("digite a primeira nota: "))
peso1 = int(input("digite o peso da sua nota"))

n2 = float(input("digite a segunda nota: "))
peso2 = int(input("digite o peso da sua nota"))

n3 = float(input("digite a terceira nota: "))
peso3 = int(input("digite o peso da sua nota"))

media = ((n1 * peso1) + (n2 * peso2) + (n3 * peso3)) /( peso1 + peso2 + peso3)

print(f"a media ponderada das notas é {media:.2f}")