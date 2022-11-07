import numpy as np

import matplotlib.pyplot as plt
import tikzplotlib

# 1D plot
x = np.arange(0, 2*np.pi+0.05, 0.05)
y = np.sin(x)

fig = plt.figure()
plt.plot(x, y, linewidth=3.0, color="C1")
plt.xlabel("$x$")
plt.ylabel("$\\sin(x)$")
plt.draw()

tikzplotlib.save("/home/seb/Desktop/tikzplotlib/plots/1d_plot.tex")


# 2D plot
x1 = np.arange(0, 2*np.pi+0.05, 0.05)
x2 = np.arange(0, 2*np.pi+0.05, 0.05)
X1, X2 = np.meshgrid(x1, x2)
Y = np.sin(X1)*np.cos(X2)

fig = plt.figure()
ax = fig.add_subplot(111)
surf = ax.pcolormesh(X1, X2, Y)
fig.colorbar(surf, ax=ax)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
plt.draw()

tikzplotlib.save("/home/seb/Desktop/tikzplotlib/plots/2d_plot.tex")

plt.show()
