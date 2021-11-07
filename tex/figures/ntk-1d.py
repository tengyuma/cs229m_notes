import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 1.3, 0.01)

fig, ax = plt.subplots()

beta = 2

def fun(alpha, i):
	lf = (1.0 - alpha*(t - beta*t*t))**2
	lg = (1.0 - alpha*t)**2
	if alpha == 1:
		ax.plot(t, lf, linestyle = 'solid', label='$\hat{L}(\\bar{f}_{\\theta})$', color = 'C%d'%i)
		ax.plot(t, lg, linestyle = 'dashed', label='$\hat{L}(\\bar{g}_{\\theta})$', color = 'C%d'%i)
	else: 
		ax.plot(t, lf, linestyle = 'solid', label='$\hat{L}(\\alpha \\bar{f}_{\\theta}))$, alpha=%.f'%alpha, color = 'C%d'%i)
		ax.plot(t, lg, linestyle = 'dashed', label='$\hat{L}(\\alpha \\bar{g}_{\\theta}))$, alpha=%.f'%alpha, color = 'C%d'%i)

fun(1, 1)

fun(2, 2)

fun(5, 3)

fun(10, 4)


ax.set_ylim([0, 1.5])
ax.set(xlabel='theta', ylabel='loss',
       title='NTK regime via reparameterization')
ax.legend()

fig.savefig("ntk-1d.png")
plt.show()
