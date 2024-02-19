import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 100)                            # Definindo o X do grafico
yc = np.cos(x)                                                          # Definindo o Y do cosseno
ys = np.sin(x)                                                          # Definindo o Y do seno

plt.figure("Comparação de Cosseno e Seno", figsize=(8, 6))         # Abetura de construção de grafico
plt.subplots_adjust(
    hspace=0.505                                                        # hspace ajusta o espaçamento entre graficos
)

plt.subplot(2, 1, 1)                                              # Defini que será 'plotado' 2 linhas e 1 coluna,
plt.title("Cosseno")                                                    # este estará na coluna 1
plt.plot(x, yc, color='r', lw=1.0)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.xticks(np.arange(-2*np.pi, 2*np.pi, 1))
plt.grid()                                                              # grid adiciona as grades do grafico

plt.subplot(2, 1, 2)                                              # Este estará na coluna 2
plt.title("Seno")
plt.plot(x, ys, color='b', lw=1.0, marker=',')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.xticks(np.arange(-2*np.pi, 2*np.pi, 1))
plt.grid()

plt.show()                                                              # Fecha a construção do grafico e o 'imprime'
