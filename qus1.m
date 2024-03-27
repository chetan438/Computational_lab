clc
close all
clear all
amplitude1 =1
frequency1 = 10
amplitude2 = 2
frequency2 = 15
t= 1:0.01:10
y1= amplitude1 * sin(2*3.14* frequency1* t)
y2= amplitude2 * sin(2*3.14* frequency2* t)

combined_signal= y1+y2

plot(t,y1)
plot(t,y2)
plot(t, combined_signal)
xlabel('Time')
ylabel('Amplitude')
grid(True)
