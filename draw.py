import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = [];y = [];z = []
with open("output-hsv.txt", "r") as file:
    for line in file:
        lineStr = line.strip()
        x.append(int(lineStr.split()[-3]))
        y.append(int(lineStr.split()[-2]))
        z.append(int(lineStr.split()[-1]))
        
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()