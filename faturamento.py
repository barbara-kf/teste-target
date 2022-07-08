import json
from statistics import median

# abrir o arquivo
arquivo = open("dados.json", "r")
conteudo = arquivo.read()
dados = json.loads(conteudo)

# fechar
arquivo.close()

# nova lista removendo os dias em que o faturamento foi 0.0
dados = [item for item in dados if item['valor'] > 0.0]

# menor valor
menor = min(item['valor'] for item in dados)
print("O menor valor de faturamento ocorrido em um dia do mês: ", menor)

# maior valor
maior = max(item['valor'] for item in dados)
print("O maior valor de faturamento ocorrido em um dia do mês: ", maior)

# média
media = sum(item['valor'] for item in dados) / len(dados)

# lista removendo os dias em que o faturamento foi menor que a média
sup_media = [item for item in dados if item['valor'] > media]
print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: ", len(sup_media))
