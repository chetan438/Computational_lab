import numpy as np
import matplotlib.pyplot as plt
duration = 0.1
t=np.linspace(0,duration,duration*100)
freq1 =10
sin1 = np.sin(2*np.pi*freq1*t)
freq2 = 15
sin2 = np.sin(2*np.pi*freq2*t)
x= sin1+sin2
lw = int(input("Enter the lenght of window"))
plt.plot()
