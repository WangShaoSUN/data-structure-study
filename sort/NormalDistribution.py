import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

mu=0
sigma=1
x=np.arange(-5,5,0.1)
# print x
y=stats.norm.pdf(x,0,1)
print y
plt.plot(x,y)
plt.title("Normal Distribution $\mu$=0.0,$\sigma^2$=1.0")
plt.show()
plt.savefig("ssd.pdf")
