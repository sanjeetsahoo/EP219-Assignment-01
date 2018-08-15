import numpy as np					#import NumPy library
import matplotlib.mlab as mlab   
import matplotlib.pyplot as plt 			#import matplot Library for plotting histogram
data = np.genfromtxt('pre_primary_school_data.csv', skip_header=1, delimiter=",", dtype=int, usecols=(12, 13, 14))
#Extract data from csv file into NumPy array excluding first row and using integers from columns M, N, O
c = ((data.size)/((data.ndim)+1))			#Defining number of columns in data as c
b = np.zeros((c,1)) 					#Initiating array of zeroes with same number of columns as given data
i = 0							#Initiating counter for iteration
for row in data:			
	if row[0] != 0:					#To avoid division by zeroes
		b[i] = ((row[1] + row[2])/row[0])	#Replacing array with zeroes with number of teachers per institution
	i=i+1
final = np.hstack((data, b))				#Adding the new column to final array 
states = ((b.size))/3					#Defining number of columns for Urban, Rural and Total each
urban = np.zeros((states,1))
rural = np.zeros((states,1))
total = np.zeros((states,1))
j = 0							#Initiating counter for feeding data from b array
i = 0							#Initiating counter for columns of Urban, Rural and Total each
while (i < 35):
	rural[i] = b[j]
	urban[i] = b[j+1]
	total[i] = b[j+2] 
	j = j+3     	
	i = i+1 
plt.hist(rural)						#Plot for Rural
plt.ylabel('Number of states')
plt.xlabel('Number of teachers per school')
plt.title(r'Histogram of number states with a certain number of teachers per pre-primary school(Rural)')
plt.show()
plt.hist(urban)						#Plot for Urban
plt.ylabel('Number of states')
plt.xlabel('Number of teachers per school')
plt.title(r'Histogram of number states with a certain number of teachers per pre-primary school(Urban)')
plt.show()
plt.hist(total)						#Plot for Urban
plt.ylabel('Number of states')
plt.xlabel('Number of teachers per school')
plt.title(r'Histogram of number states with a certain number of teachers per pre-primary school(Total)')
plt.show()

