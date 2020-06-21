import matplotlib.pyplot as plt
import numpy as np


lines_closest_package_first = open('results/result_closest_package_first.txt', 'r').readlines()
lines_next_closest = open('results/result_next_closest.txt', 'r').readlines()
lines_random = open('results/result_random.txt', 'r').readlines()
lines_multiple_packages = open('results/result_multiple_packages.txt', 'r').readlines()

steps_random = []
steps_next_closest = []
steps_closest_package_first = []
steps_multiple_packages = []

for line in lines_random:
    steps_random.append(int(line.split('= ')[-1]))
for line in lines_next_closest:
    steps_next_closest.append(int(line.split('= ')[-1]))
for line in lines_closest_package_first:
    steps_closest_package_first.append(int(line.split('= ')[-1]))
for line in lines_multiple_packages:
    steps_multiple_packages.append(int(line.split('= ')[-1]))

x = np.arange(len(steps_random)) #Same as number of runs
ax = plt.subplot(111)

# ax.bar(x+0.4, steps_closest_package_first, color='b', align='center', label='closest_package_first', width=0.2)
ax.bar(x+0.2, steps_next_closest, color='r', align='center', label = 'next closest', width=0.2)
# ax.bar(x-0.2, steps_random, color = 'y', align = 'center', label = 'random', width = 0.2)
ax.bar(x, steps_multiple_packages, color = 'b', align = 'center', label = 'multiple_packages', width = 0.2)
plt.xlabel('run number')
plt.ylabel('number of steps till done')
plt.legend(loc = 'lower right')
plt.show()