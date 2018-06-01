from matplotlib import pyplot as plt
import numpy as np
from scipy import signal

x = np.arange(0, 10*np.pi, .01)
y = np.sin(x)
y2 = np.sin(x/2)

# print(x)

s = signal.square(y)
s2 = signal.square(y2)
s = np.interp(s, (s.min(), s.max()), (0, +1))
s2 = np.interp(s2, (s2.min(), s2.max()), (0, +1))


plt.figure(1)
plt.plot(x,y)
plt.plot(x, s, 'r')

# plt.show()
plt.savefig("square_sig.png")

plt.figure(2)

plt.subplot(3,1,1)
plt.plot(x, s, 'g')
plt.subplot(3,1,2)
plt.plot(x, s2, 'b')
plt.subplot(3,1,3)
plt.plot(x,np.logical_or(s,s2),'r')
plt.savefig("two_square.png")

plt.figure(3)

x1hz = np.arange(0, 2*np.pi, .01)
y1hz = np.sin(x1hz)
plt.plot(x1hz,y1hz)
plt.savefig("1hz.png")