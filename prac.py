
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.xticks(rotation = "vertical") # Rotates X-Axis Ticks by 45-degrees
plt.show()