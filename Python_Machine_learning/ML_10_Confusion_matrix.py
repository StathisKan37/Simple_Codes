import numpy
import matplotlib.pyplot as plt
from sklearn import metrics

# Generating the numbers for actual and predicted values
# actual values: val_act
# predicted values: val_pred
val_act = numpy.random.binomial(1,.9,size = 1000)
val_pred = numpy.random.binomial(1,.9,size = 1000)

# Using the confusion matrix function
confusion_matrix = metrics.confusion_matrix(val_act, val_pred)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [0, 1])

# Printing the proportion of correct predictions
print(f'Accuracy: {metrics.accuracy_score(val_act, val_pred)}')
print(f'Precision: {metrics.precision_score(val_act, val_pred)}')
print(f'Sensitivity recall: {metrics.recall_score(val_act, val_pred)}')
print(f'Specificity: {metrics.recall_score(val_act, val_pred, pos_label=0)}')
print(f'F1_score: {metrics.f1_score(val_act, val_pred)}')

# Displaying the plot
cm_display.plot()
plt.show()

# SOURCE:
# https://www.w3schools.com/python/python_ml_confusion_matrix.asp
