# Define a function called plot_timeseries
def plot_timeseries(axes, x, y, color, xlabel, ylabel):

  # Plot the inputs x,y in the provided color
  axes.plot(x, y, color=color)

  # Set the x-axis label
  axes.set_xlabel(xlabel)

  # Set the y-axis label
  axes.set_ylabel(ylabel, color=color)

  # Set the colors tick params for y-axis
  axes.tick_params('y', colors=color)

'''
O código acima demonstra como definir uma função chamada `plot_timeseries` que recebe vários parâmetros para plotar uma série temporal em um gráfico Matplotlib. A função plota os dados fornecidos (x e y) em uma cor específica, define os rótulos dos eixos x e y, e ajusta a cor dos ticks do eixo y para corresponder à cor da linha do gráfico. Isso facilita a criação de gráficos de séries temporais personalizados com diferentes variáveis e estilos visuais.
'''