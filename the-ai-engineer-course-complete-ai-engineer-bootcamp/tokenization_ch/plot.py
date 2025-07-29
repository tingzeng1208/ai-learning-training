import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [i ** 2 for i in x]

plt.plot(x, y)
plt.title('Simple Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)

plt.show()