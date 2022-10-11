import numpy as np
import matplotlib.pyplot as plt

array = np.arange(5,15)
print(array)
print()

array = np.linspace(0,23,7, endpoint = True)
print(array)
print()

 
my_list = -1 + 2 * np.random.rand(10)
print(my_list)
print()

x = np.arange(0, 1, 0.1);
y = np.sin(x)
plt.plot(x, y,'o')
plt.show()

vec1 = np.random.random(size = 10)
vec2 = np.random.random(size = 10)
dist = np.linalg.norm(vec1 - vec2)
print(vec1)
print()
print(vec2)
print()
print(dist)