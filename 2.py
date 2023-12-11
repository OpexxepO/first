import matplotlib.pyplot as plt 
import numpy as np 
f = np.linspace(30, 141, 1000)
R1 = 10
E = 10
R2 = 0.2
R3 = R2
I0 = []
Ur = []
Ul = []
Uc = []
L1 = 100 * 10 ** (-3)
L2 = 25 * 10 ** (-3)
C1 = 110 * 10 ** (-6)
C2 = C1
w = 2 * np.pi
for i in range(0, len(f)):
	i0 = E / np.sqrt(R1 ** 2 + (w * f[i] * L1 - 1 / (w * f[i] * C1)) ** 2)
	I0.append(i0)
	ur = i0 * R1
	Ur.append(ur)
	ul = i0 * w * L1 * f[i]
	Ul.append(ul)
	uc = i0 * (1 / (w * C1 * f[i])) 
	Uc.append(uc)

plt.plot(f, I0, 'r', label="I0")
plt.plot(f, Ur, 'b', label="Ur")
plt.plot(f, Ul, 'g', label="Ul")
plt.plot(f, Uc, 'y', label="Uc")

plt.plot(48, max(I0), 'o')
plt.plot(48, max(Ur),  'o')
plt.plot(48, max(Ul),  'o')
plt.plot(48, max(Uc), 'o')
plt.legend()
plt.grid()
plt.show()

I = []
I1 = []
I2 = []
for i in range(len(f)):
	i1 = E / np.sqrt(R2 ** 2 + (w * f[i] * L2) ** 2)
	I1.append(i1)
	i2 = E / np.sqrt(R3 ** 2 + (1 / (w * f[i] * C2)) ** 2)
	I2.append(i2)
	phi1 = np.arctan(w * L2 * f[i] / R2)
	phi2 = np.arctan(-1 / (w * f[i] * C2)/ R3)
	i = np.sqrt(i1 ** 2 + i2 ** 2 + 2 * i1 * i2 * np.cos(phi2- phi1))
	I.append(i)

plt.plot(f, I1, 'r', label="I1")
plt.plot(f, I2, 'b', label="I2")
plt.plot(f, I, 'g', label="I")
plt.plot(96, 0.666, 'o')
plt.plot(96, 0.661,  'o')
plt.plot(96, min(I),  'o')
plt.legend()
plt.grid()
plt.show()
