# Created by Levi Grantz

import numpy as np
import matplotlib.pyplot as plt

count = np.arange(0, 50)  # number of data points

# data for food and snake at fixed positions while varying map size
X3 = np.loadtxt('SnakeGameData_FixedFood3x3.txt')
X4 = np.loadtxt('SnakeGameData_FixedFood4x4.txt')
X5 = np.loadtxt('SnakeGameData_FixedFood5x5.txt')
X6 = np.loadtxt('SnakeGameData_FixedFood6x6.txt')
X7 = np.loadtxt('SnakeGameData_FixedFood7x7.txt')
X8 = np.loadtxt('SnakeGameData_FixedFood8x8.txt')

# data for fixed map size while varying distance between snake and food
X81 = np.loadtxt('SnakeGameData_Distance1.txt')
X82 = np.loadtxt('SnakeGameData_Distance2.txt')
X83 = np.loadtxt('SnakeGameData_Distance3.txt')
X84 = np.loadtxt('SnakeGameData_Distance4.txt')
X85 = np.loadtxt('SnakeGameData_Distance5.txt')
X86 = np.loadtxt('SnakeGameData_Distance6.txt')
X87 = np.loadtxt('SnakeGameData_Distance7.txt')


# varying map size histograms
n0, bins0, edges0 = plt.hist(X3, edgecolor='black')
plt.title('3x3 Data')
plt.xlabel('Number of Steps')
plt.xticks(bins0)
plt.show()

n1, bins1, edges1 = plt.hist(X4, edgecolor='black')
plt.title('4x4 Data')
plt.xlabel('Number of Steps')
plt.xticks(bins1)
plt.show()

n2, bins2, edges2 = plt.hist(X5, edgecolor='black')
plt.title('5x5 Data')
plt.xlabel('Number of Steps')
plt.xticks(bins2)
plt.show()

n3, bins3, edges3 = plt.hist(X6, edgecolor='black')
plt.title('6x6 Data')
plt.xlabel('Number of Steps')
plt.xticks(bins3)
plt.show()

n4, bins4, edges4 = plt.hist(X7, edgecolor='black')
plt.title('7x7 Data')
plt.xlabel('Number of Steps')
plt.xticks(bins4)
plt.show()

n5, bins5, edges5 = plt.hist(X8, edgecolor='black')
plt.title('8x8 Data')
plt.xlabel('Number of Steps')
plt.xticks(bins5)
plt.show()

# distance histograms
n6, bins6, edges6 = plt.hist(X81, edgecolor='black')
plt.title('Distance from Food = 1')
plt.xlabel('Number of Steps')
plt.xticks(bins6)
plt.show()

n7, bins7, edges7 = plt.hist(X82, edgecolor='black')
plt.title('Distance from Food = 2')
plt.xlabel('Number of Steps')
plt.xticks(bins7)
plt.show()

n8, bins8, edges8 = plt.hist(X83, edgecolor='black')
plt.title('Distance from Food = 3')
plt.xlabel('Number of Steps')
plt.xticks(bins8)
plt.show()

n9, bins9, edges9 = plt.hist(X84, edgecolor='black')
plt.title('Distance from Food = 4')
plt.xlabel('Number of Steps')
plt.xticks(bins9)
plt.show()

n10, bins10, edges10 = plt.hist(X85, edgecolor='black')
plt.title('Distance from Food = 5')
plt.xlabel('Number of Steps')
plt.xticks(bins10)
plt.show()

n11, bins11, edges11 = plt.hist(X86, edgecolor='black')
plt.title('Distance from Food = 6')
plt.xlabel('Number of Steps')
plt.xticks(bins11)
plt.show()

n12, bins12, edges12 = plt.hist(X87, edgecolor='black')
plt.title('Distance from Food = 7')
plt.xlabel('Number of Steps')
plt.xticks(bins12)
plt.show()


# means and STDS for varying maps size
print('Mean of X3: {:.4f}'.format(np.mean(X3)))
print('Standard Deviation of X3: {:.4f}'.format(np.std(X3)))

print('Mean of X4: {:.4f}'.format(np.mean(X4)))
print('Standard Deviation of X4: {:.4f}'.format(np.std(X4)))

print('Mean of X5: {:.4f}'.format(np.mean(X5)))
print('Standard Deviation of X5: {:.4f}'.format(np.std(X5)))

print('Mean of X6: {:.4f}'.format(np.mean(X6)))
print('Standard Deviation of X6: {:.4f}'.format(np.std(X6)))

print('Mean of X7: {:.4f}'.format(np.mean(X7)))
print('Standard Deviation of X7: {:.4f}'.format(np.std(X7)))

print('Mean of X8: {:.4f}'.format(np.mean(X8)))
print('Standard Deviation of X8: {:.4f}'.format(np.std(X8)))

# means and STDs for distances
print('Mean of X81: {:.4f}'.format(np.mean(X81)))
print('Standard Deviation of X81: {:.4f}'.format(np.std(X81)))

print('Mean of X82: {:.4f}'.format(np.mean(X82)))
print('Standard Deviation of X82: {:.4f}'.format(np.std(X82)))

print('Mean of X83: {:.4f}'.format(np.mean(X83)))
print('Standard Deviation of X83: {:.4f}'.format(np.std(X83)))

print('Mean of X84: {:.4f}'.format(np.mean(X84)))
print('Standard Deviation of X84: {:.4f}'.format(np.std(X84)))

print('Mean of X85: {:.4f}'.format(np.mean(X85)))
print('Standard Deviation of X85: {:.4f}'.format(np.std(X85)))

print('Mean of X86: {:.4f}'.format(np.mean(X86)))
print('Standard Deviation of X86: {:.4f}'.format(np.std(X86)))

print('Mean of X87: {:.4f}'.format(np.mean(X87)))
print('Standard Deviation of X87: {:.4f}'.format(np.std(X87)))