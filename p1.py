import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10,0.01)
y1 = np.sin(x)
y2 = np.cos(x)
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(1,1,1)
ax.set_xlim([-4, 4])
ax.set_ylim ([-2, 2])
ax.plot(x,y1, color='blue', linewidth=2,
label='sin(x)')
ax.plot(x,y2, color='red', linewidth=2,
label='cos(x)')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.grid()
plt.title('sin(x) and cos(x)')
plt.legend(loc='lower right')
plt.show0