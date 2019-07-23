import matplotlib.pyplot as plt
import numpy as np

def random_plots():
  xs = []
  ys = []
  
  for i in range(20):
    x = i
    y = np.random.randint(10)
    
    xs.append(x)
    ys.append(y)
  
  return xs, ys

fig = plt.figure()
ax2 = plt.subplot2grid((5, 2), (1, 0), rowspan=3, colspan=2)

x, y = random_plots()
ax2.plot(x, y)

plt.tight_layout()
plt.show()
