import random
import matplotlib.pyplot as plt

x = [random.randint(1,10) for _ in range(10)]
y = [random.randint(1,10) for _ in range(10)]

fig, ax = plt.subplots()
ax.scatter(x, y)

fig
