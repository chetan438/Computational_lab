import matplotlib.pyplot as plt
import numpy as np

amplitude1 =1
frequency1 = 10
amplitude2 = 2
frequency2 = 15
t= np.linspace(0, 10, int(10*1000))
y1= amplitude1 * np.sin(2*np.pi* frequency1* t)
y2= amplitude2 * np.sin(2*np.pi* frequency2* t)

combined_signal= y1+y2

plt.plot(t,y1, label='Sinusoid 1 (f = 10 HZ)')
plt.plot(t,y2, label='Sinusoid 2 (f = 15 HZ)')
plt.plot(t, combined_signal, label='Combined Signal')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.title('Sum of two sinusoids')
plt.grid(True)
plt.legend()
plt.show()
