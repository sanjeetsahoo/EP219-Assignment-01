import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt



data = np.genfromtxt('pre_primary_school_data.csv', skip_header=1, delimiter=",", dtype=int, usecols=(12, 13, 14))
#print(data)
i = 0
c = ((data.size)/((data.ndim)+1))
#print(c)
b = np.zeros((c,1))
#print(b)
for row in data:
	if row[0] != 0:
		b[i] = ((row[1] + row[2])/row[0])
		#print(b[i])
	i=i+1
#print(data.shape)
#print(b.shape)
final = np.hstack((data, b))
#print(final)
j = 0
i = 0
states = ((b.size))/3
urban = np.zeros((states,1))
rural = np.zeros((states,1))
total = np.zeros((states,1))
#print(b.shape)
#print(urban.shape)
#print(b)
while (i < 35):
	rural[i] = b[j]
	urban[i] = b[j+1]
	total[i] = b[j+2] 
	j = j+3     	
	i = i+1 	
	#print(i)
	#print(j)
#print(urban)
#print(rural)
#print(total)
plt.hist(rural)
plt.ylabel('Number of states')
plt.xlabel('Number of teachers per school')
plt.title(r'Histogram of number states with a certain number of teachers per pre-primary school(Rural)')
plt.show()
plt.hist(urban)
plt.ylabel('Number of states')
plt.xlabel('Number of teachers per school')
plt.title(r'Histogram of number states with a certain number of teachers per pre-primary school(Urban)')
plt.show()
plt.hist(total)
plt.ylabel('Number of states')
plt.xlabel('Number of teachers per school')
plt.title(r'Histogram of number states with a certain number of teachers per pre-primary school(Total)')
plt.show()

