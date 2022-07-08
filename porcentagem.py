# dicionário com as cidades
cidades = {"SP":67836.43, "RJ":36678.66, "MG":29229.88, "ES":27165.48, "Outros":19849.53}

# somar os valores
total = sum(cidades.values())

# função pra calcular a porcentagem
def porcentagem(parte, total):
    porcentagem = 100 * float(parte)/float(total)
    return "{:0.2f}%".format(porcentagem)

# loop pra percorrer o dicionário calculando com a função
for k, v in cidades.items():
    print(k, "representa", porcentagem(v, total), "do valor total mensal da distribuidora.")