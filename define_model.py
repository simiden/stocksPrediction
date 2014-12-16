#coding=utf-8

import math

def update(pos):
	k = len(pos) - 1
	pos[k] = pos[k] + 1
	while (k > 0 && pos[k] >= 3):
		pos[k-1] = pos[k-1] + 1
		pos[k] = 0

	return pos

def function_y(pos):
	ans = pos[0]
	for j in range(1, len(pos)):
		pos
class type_model:
	
	def __init__(self, num):
		temp = 1
		for i in range(num):
			temp = temp * 3
		self.neuron_num = [num, num*3, temp, temp, temp, 1]
		self.bell_func_parameters = [[0.5 for col in range(3)] for row in range(num)]
		self.matrixK = [0.1 for col in range((num+1)*temp)]
		self.data = [0 for one in range(6)]
		for i in range(6):
			self.data[i] = [0 for row in range(self.neuron_num[i])]

	def train_model(self, history):
		"""
		Training the data of ten days. 
		To predict the trendency of the next day and the next week.
		"""

		error = 10000;
		epoch = 0;
		while (error > 0.001):
			epoch = epoch + 1
			matrixA = []
			yd = []
			for i in range(self.input_num, len(history)):
				calc_layer0(history[i-self.input_num:i])		
				calc_layer1()
				calc_layer2()
				calc_layer3()
				
				line = []
				item = []
				p = 0
				for j in range(self.neuron_num[3]):
					item[p] = self.data[3][j]
					p = p + 1
					for k in range(self.neuron_num[0]):
						item[p] = self.data[3][j] * self.data[0][k]
						p = p + 1
					line = line + item
				matrixA[i-self.input_num] = line
				yd[i.input_num] = history[i]['Adj Close']

			
				
	def run_model(self, history):
		calc_layer0(history)
		calc_layer1()
		calc_layer2()
		calc_layer3()
		calc_layer4()
		calc_layer5()
	
	def calc_layer0(self, history):
		max_data = -10
		min_data = 100000000
		for j in range(self.neuron_num[0]):
			self.data[0][j] = history[j]['Adj Close']
			max_data = max(max_data, self.data[0][j])
			min_data = min(min_data, self.data[0][j])

		for j in range(self.neuron_num[0]):
			self.data[0][j] = (self.data[0][j] - min_data) / (max_data - min_data)

	def calc_layer1(self):
		for j in range(self.neuron_num[1]):
			s0 = self.bell_func_parameters[j/3][0];
			s1 = self.bell_func_parameters[j/3][1]					
			s2 = self.bell_func_parameters[j/3][2];
					
			x = self.data[0][j/3]
			t = j % 3;				
			if t == 0:
				self.data[1][j] = -1 / (1 + math.exp(-s1*(x-s2)))
			if t == 1:
				self.data[1][j] = 1 / (1 + math.exp(-s1*(x-s2))) - 1 / (1 + math.exp(-s1*(x-s3)))
			if t == 2:
				self.data[1][j] = 1 / (1 + math.exp(-s1*(x-s3)))

	def calc_layer2(self):
		pos = [0 for one in range(self.neuron_num[0])]
		pos[self.neuron_num[0]-1] = -1

		for j in range(self.neuron_num[2]):
			pos = update(pos)
			self.data[2][j] = 1
			for k in range(len(pos)):
				self.data[2][j] = self.data[2][j] * self.data[1][pos[k]]

	def calc_layer3(self):
		sum = 0.0
		for j in range(self.neuron_num[2]):
			sum = sum + self.data[2][j]
		for j in range(self.neuron_num[3]):
			self.data[3][j] = self.data[3][j] / sum

	def calc_layer4(self):
		pos = [0 for one in range(self.neuron_num[0])]
		pos[self.neuron_num[0]-1] = -1

		p = 0
		for j in range(self.neuron_num[4]):
			pos = update(pos)
			y = self.matrixK[p]
			p = p + 1
			for k in range(0, len(pos)):
				y = y + self.matrixK[p]*self.data[0][k]
				p = p + 1
			self.data[4][j] = y * self.data[3][j]

	def calc_layer5(self):
		self.data[5][0] = 0
		for j in range(self.neuron_num[5]):
			self.data[5][0] = self.data[5][0] + self.data[4][j]


