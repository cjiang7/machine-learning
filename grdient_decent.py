#!/usr/local/bin/python3

import pandas as pd
import numpy as np

def cost(x, y, t1, t2, m):
	return 0.5*m*sum([((t1+t2*np.asarray([x[i]])) - y[i])**2 for i in range(m)]) 

def converge(x,y,m,alpha,times=1500,t1=0,t2=0):
	
	new_t1 = t1
	new_t2 = t2
	error_list = []

	for time in range(times):
		t1_sum = (1.0/m) * sum([((new_t1+new_t2*np.asarray([x[i]])) - y[i]) for i in range(m)])
		t2_sum = (1.0/m) * sum([((new_t1+new_t2*np.asarray([x[i]])) - y[i])*np.asarray([x[i]]) for i in range(m)])
		new_t1 = new_t1 - alpha * t1_sum
		new_t2 = new_t2 - alpha * t2_sum
		error = cost(x,y,new_t1,new_t2,m)
		error_list.append(error)

if __name__ == '__main__':
	data = pd.read_csv('liner_re.data', names=['x','y'])

	x = data['x']
	y = data['y']
	m = x.shape[0]
	
	alpha = 0.01
	converge(x,y,m,alpha,times=1500,t1=0,t2=0)

