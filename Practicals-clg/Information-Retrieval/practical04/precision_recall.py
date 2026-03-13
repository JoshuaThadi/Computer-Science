# part-2 (precision_recall_fmeasure.py)

def calculate_metrics(retrieved_set, relevant_set):
 true_positive = len(retrieved_set.intersection(relevant_set))
 false_positive = len(retrieved_set.difference(relevant_set))
 false_negative = len(relevant_set.difference(retrieved_set))
 '''
 (Optional)
 PPT values:
 true_positive = 20
 false_positive = 10
 false_negative = 30
 '''
 print("True Positive: ", true_positive
 ,"\nFalse Positive: ", false_positive
 ,"\nFalse Negative: ", false_negative ,"\n")
 precision = true_positive / (true_positive + false_positive)
 recall = true_positive / (true_positive + false_negative)
 f_measure = 2 * precision * recall / (precision + recall)
 return precision, recall, f_measure
retrieved_set = set(["doc1", "doc2", "doc3"]) #Predicted set
relevant_set = set(["doc1", "doc4"]) #Actually Needed set (Relevant)
precision, recall, f_measure = calculate_metrics(retrieved_set, relevant_set)
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F-measure: {f_measure}")
print("\nPerformed by Joshua Thadi 48")