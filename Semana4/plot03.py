import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Basic Graph


x = [0,1,2,3,4]
y = [0,2,4,6,8]

# redimensionando o grafico 
plt.figure(figsize=(5,3), dpi=100)

# plota o grafico incrementado
# plt.plot(x,y, label='2x', color='red', linewidth=2, marker='.', linestyle='--', markersize=10, markeredgecolor='blue')
# plota o grafico colocando uma legenda com 2x e marcador  
plt.plot(x,y, 'b^--', label='2x')

# seta o intervalo de pontos que iremos plotar 
x2 = np.arange(0,4.5,0.5)

# plotando a parte do grafico linear
plt.plot(x2[:6], x2[:6]**2, 'r', label='X^2')
# plotando a parte do grafico ao quadrado
plt.plot(x2[5:], x2[5:]**2, 'r--')

# Titulo do grafico
plt.title('Primeiro Grafico!', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})

# Nome do eixo X e Y
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Escala do gráfico e deixando o eixo X s/ decimal
plt.xticks([0,1,2,3,4,])
#plt.yticks([0,2,4,6,8,10])

# adiciona legenda ao grafico
plt.legend()

# salva a figura 
plt.savefig('mygraph.png', dpi=300)

# mostra a plotagem
plt.show()
