import torch
import torch.nn as nn
import torch.nn.functional as F

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Neural network:
# Input layer: inl (neurons: 4)
# Hidden layer 1: hl1 (neurons: 8)
# Hidden layer 2: hl2 (neurons: 9)
# Output layer: outl (neurons: 3)

# A Model class to inherit nn.Module
class Model(nn.Module):
	def __init__(self, inl=4, hl1=8, hl2=9, outl=3):
		# Instantiating the nn.Module
		super().__init__()
		self.fc1 = nn.Linear(inl, hl1)
		self.fc2 = nn.Linear(hl1, hl2)
		self.fcout = nn.Linear(hl2, outl)
	
	def forward(self, x):
		x = F.relu(self.fc1(x))
		x = F.relu(self.fc2(x))
		x = F.relu(self.fcout(x))
		return x

# Picking a random seed (41)
torch.manual_seed(41)

# Creating an instance of model
model = Model()

# Loading the irish dataset
# Source: https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv
dataframe = pd.read_csv('Iris_Dataset.csv')
print('IRIS DATASET:\n')
print(dataframe)
print('---------------------------------------------------------------------')

# Replacing all strings with integers
dataframe['species'] = dataframe['species'].replace('setosa', 0.0)
dataframe['species'] = dataframe['species'].replace('versicolor', 1.0)
dataframe['species'] = dataframe['species'].replace('virginica', 2.0)
print('IRIS DATASET WITH NUMBERS ONLY:\n')
print(dataframe)
print('     Setosa --> 0')
print(' Versicolor --> 1')
print('  Virginica --> 2')
print('---------------------------------------------------------------------')

# Splitting data to X and Y
X = dataframe.drop('species', axis=1)
Y = dataframe['species']

# Splitting data to trainning and testing
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=41)

# Converting features to FloatTensor or LongTensor
X_train = torch.FloatTensor(X_train.values)
X_test = torch.FloatTensor(X_test.values)
Y_train = torch.LongTensor(Y_train.values)
Y_test = torch.LongTensor(Y_test.values)

# Setting the criterion of model to measure
# How far off are the predictions from the data
criterion = nn.CrossEntropyLoss()

# Choose Adam Optimizer
# lr: learning rate
# if error doesn't go down after a bunch of interations (epochs)
# lower our learning rate
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
print('MODEL PARAMETERS:')
print(model.parameters)
print('---------------------------------------------------------------------')
print('EPOCH AND LOSS OF MODEL:')

# Training the model
# Epochs? (one run thru all the training data in our network)
epochs = 100
losses = []
for i in range(epochs):
	# Go forward and get a prediction
	# Getting predicted rsults
	Y_pred = model(X_train)
	
	# Measure the loss/error, gonna be high at first
	# Predicted values vs Y_train
	loss = criterion(Y_pred, Y_train)
	
	# Keeping track of our losses
	losses.append(loss.detach().numpy())
	
	# Printing every 10 epoch
	if (i%10 == 0):
		print(f'Epoch: {i} and loss: {loss}')
	
	# Doing some back propagation: take the error rate of forward
	# propagation and feed it back thru the network to fine tune the weights
	optimizer.zero_grad()
	loss.backward()
	optimizer.step()
print('---------------------------------------------------------------------')

# Graph it
plt.plot(range(epochs), losses)
plt.ylabel('loss/error')
plt.xlabel('Epoch')
plt.show()

# Evaluating Model on Test Data set
# (variable model on test set)
# Turning off back propogation
with torch.no_grad():
	# X_test: Featuresfrom test set
	# Y_eval: Predictions
	Y_eval = model.forward(X_test)
	# Finding the loss or error
	loss = criterion(Y_eval, Y_test)
print('LOSS ON THE TEST SET:')
print(loss)
print(loss.item())
print('---------------------------------------------------------------------')

correct = 0
with torch.no_grad():
	for i, data in enumerate(X_test):
		Y_val = model.forward(data)
		
		if Y_test[i] == 0:
			x = "Setosa"
		elif Y_test[i] == 1:
			x = 'Versicolor'
		else:
			x = 'Virginica'
		
		# Printing the type of flower class our network think it is
		print(f'{i+1}.)  {str(Y_val)} \t {x} \t {Y_val.argmax().item()}')
		
		# Correct or not
		if (Y_val.argmax().item() == Y_test[i]):
			correct += 1
print(f'There are {correct} correct')
print('---------------------------------------------------------------------')

print('FEEDING NEW DATA:')
# Creating new Iris data point
new_iris_1 = torch.tensor([4.7, 3.2, 1.3, 0.2])
# Feeding data point through the network
with torch.no_grad():
	print(model(new_iris_1))

new_iris_2 = torch.tensor([5.9, 3.0, 5.1, 1.8])
with torch.no_grad():
  print(model(new_iris_2))
print('---------------------------------------------------------------------')

# Saving the NN Model
torch.save(model.state_dict(), 'IRIS_MODEL.pt')

# Load the Saved Model
new_model = Model()
new_model.load_state_dict(torch.load('IRIS_MODEL.pt'))
