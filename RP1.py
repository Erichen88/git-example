import numpy as np
import matplotlib.pyplot as plt

N=100  # Number of end point od the grid including T
T=1      # Length of the interval [0 , T] in time units
delta = T / N  # time increment
w = np.zeros(N+1) # initialization of the vector W
t = np.arange(0, T+1/ N, 1/N) # 系列 0~T 每 1/N 為一段

#模擬 30 條 Wiener process 
for i in range(30):
    for j in range(1, (N+1)):
        z = np.random.normal(0,1) # 標準常態分配的隨機數
        w[j] = w[j-1] + z * np.sqrt(delta)
    plt.plot(t,w)
    plt.title('Wiener process')

