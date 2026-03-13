# part-1 (average_precision.py)

from sklearn.metrics import average_precision_score
y_true = [0, 1, 1, 0, 1, 1] #Binary Prediction
y_scores = [0.1, 0.4, 0.35, 0.8, 0.65, 0.9] #Model's estimation score
average_precision = average_precision_score(y_true, y_scores)
print(f'Average precision-recall score: {average_precision}')
print("\nPerformed by Joshua Thadi 48")