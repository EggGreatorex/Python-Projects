
import random
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')



def animate(i):
    data = pd.read_csv('./excelFiles/data9.csv')
    x = data['x_value']
    y1 = data['total_1'] # E.G. YT CHANNEL 1
    y2 = data['total_2']# E.G. YT CHANNEL 2
    plt.cla()
    plt.plot(x,y1,label="Channel 1")
    plt.plot(x,y2,label="Channel 2")
    plt.legend(loc='upper left')
    plt.xlabel("Seconds")
    plt.ylabel("Subscriber Count")
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(),animate, interval=300) # Interval =  300 is the parameter passed into animate


plt.tight_layout()
plt.show()




