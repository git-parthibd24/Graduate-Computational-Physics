#A sample of dry battery cells tested to find the length of life produced the following result: xmean = 12 hours, standard deviation = 3 hours. Assuming that the data are normally distributed, what percentage of battery are expected to have life between 10-14 hours?
#Method 2

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(x):
	return 1/(np.sqrt(2*np.pi)*sig)*np.exp((-(x-mu)**2)/(2*sig**2))

mu,sig=12,3
low,up=10,14

print('The percentage of cells with battery life between',low,'and',up,'hours is :',quad(f,low,up)[0]*100,'%')