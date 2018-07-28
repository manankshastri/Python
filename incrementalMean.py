import numpy as np

def incremental_mean(x):
	mu = 0
	mean_values = []
	for k in range(0, len(x)):
		mu = mu + (1.0/(k+1))*(x[k] - mu)
		mean_values.append(mu)
	return 	mean_values

mean_values([1, 2, 3, 4, 5])	