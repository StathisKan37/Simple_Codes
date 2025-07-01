import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Reading the .csv file 'comedians_data.csv'
dataframe = pandas.read_csv('comedians_data.csv')

# Converting the non numerical columns into numerical values
dictionary = {'UK': 0, 'USA': 1, 'N': 2}
dataframe['Nationality'] = dataframe['Nationality'].map(dictionary)
dictionary = {'YES': 1, 'NO': 0}
dataframe['Go'] = dataframe['Go'].map(dictionary)
print(dataframe)

# Feature columns (X): [Age, Experience, Rank, Nationality]
# Target column (y): [Go]
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = dataframe[features]
y = dataframe['Go']

# Creating and training the decision tree classifier
decision_tree = DecisionTreeClassifier()
decision_tree = decision_tree.fit(X, y)

# Making two predictions
print('EXAMPLE_1:')
prediction_1 = decision_tree.predict([[40, 10, 7, 1]])
print('Should I go to a show starring a 40 years old American comedian, with 10 years of experience, and a comedy ranking of 7?')
print(f'Answer:{prediction_1}')

print('EXAMPLE_2:')
prediction_2 = decision_tree.predict([[40, 10, 6, 1]])
print('Should I go to a show starring a 40 years old American comedian, with 10 years of experience, and a comedy ranking of 6?')
print(f'Answer:{prediction_2}')

print("[1] means 'GO'")
print("[0] means 'NO'")

# Plotting the tree
plot_tree(decision_tree, feature_names=features, filled=True)
plt.show()

# SOURCE:
# https://www.w3schools.com/python/python_ml_decision_tree.asp
