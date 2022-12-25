
import numpy as np  
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def DrawBubble (read_name): # Пузырьковая диаграмма
         sns.set (style = "whitegrid") # Установить стиль
         fp = pd.read_csv (read_name) # источник данных
         x = fp.people # данные оси X
         y = fp.price # данные по оси Y
         z = fp.price # используется для настройки размера каждой точки s
    cm = plt.cm.get_cmap('RdYlBu')
    fig,ax = plt.subplots(figsize = (12,10))
         # Обратите внимание на метод дискретизации, ведь вам нужно интуитивно чувствовать ценность точки через размер точки
         # Я использую значение текущей точки минус минимальное значение в наборе +0,1, а затем * 1000
         # Параметры: данные по оси X, данные по оси Y, размер каждой точки и цвет каждой точки.
    bubble = ax.scatter(x, y , s = (z - np.min(z) + 0.1) * 1000, c = z, cmap = cm, linewidth = 0.5, alpha = 0.5)
    ax.grid()
    fig.colorbar(bubble)
         ax.set_xlabel ('люди городов', fontsize = 15) # подпись оси X
         ax.set_ylabel ('price of something', fontsize = 15) # подпись оси Y
    plt.show()
if __name__=='__main__':
         DrawBubble ("PeopleNumber.csv") # Пузырьковая диаграмма
