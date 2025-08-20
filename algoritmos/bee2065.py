from bisect import insort

n, m = map(int, input().split())
tempos_caixas = list(map(int, input().split()))
clientes = list(map(int, input().split()))

caixas = [[0, i] for i in range(n)]
caixas.sort()

for produtos in clientes:
    tempo_livre, id_caixa = caixas.pop(0)
    tempo_livre += produtos * tempos_caixas[id_caixa]
    insort(caixas, [tempo_livre, id_caixa])

print(caixas[n-1][0])
