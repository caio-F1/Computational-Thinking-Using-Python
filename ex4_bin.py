dec = int(input("Informe o numero ibteiro positivo: "))

while dec < 0:
    print("numero invalido! ")
    dec = int(input("informe o  umero inteiro positivo: "))
    
binario = 0
pot10 = 1
while dec != 0:
    resto = dec % 2 
    binario = binario + resto * pot10
    dec = dec // 2
    pot10 = pot10 * 10

print(binario)

