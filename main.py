import matplotlib.pyplot as plt

# Lista vazia para armazenar as coordenadas
coordenadas = []

# Define o tamanho do plano cartesiano
tamanho_plano = 10

# Loop para coletar as coordenadas do usuário
print("Digite 3 cordenadas:")
for i in range(3):
    x = input("X: ")
    y = input("Y: ")
    print("Cordenada "+str(i+1)+": ("+x+","+y+")")
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print("As coordenadas devem ser números!")
        continue
    if abs(x) > tamanho_plano or abs(y) > tamanho_plano:
        print("As coordenadas estão fora do limite do plano cartesiano!")
        continue
    coordenadas.append((x, y))

# Cria uma figura
fig, ax = plt.subplots()

# Printa cada ponto coletado do usuário
for coord in coordenadas:
    ax.plot(coord[0], coord[1], marker='o', markersize=10, color='red')

# Configura os limites do plano cartesiano
ax.set_xlim([-tamanho_plano, tamanho_plano])
ax.set_ylim([-tamanho_plano, tamanho_plano])

# Exibe o gráfico
plt.show()

# Printa cordenadas inseridas pelo usuario
print("Suas coordenadas são:")

if coordenadas: # se a lista não for vazia
    separador = ' '
    print(separador.join(map(str, coordenadas)))

