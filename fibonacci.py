# informar o número
num = int(input("Digite o número que deseja verificar: "))

# início em 0 e 1
a = 0
b = 1

# como podem inserir qualquer número, fazer a sequência até enquanto o último número calculado seja menor ou igual inserido
while b <= num:
    c = a + b
    a = b
    b = c

# verificar se pertence ou não
if b==num:
    print("O número pertence à sequência.")
else:
    print("O número não pertence à sequência.")
