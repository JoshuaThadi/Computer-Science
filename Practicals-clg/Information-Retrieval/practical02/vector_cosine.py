# part-2 (vectorspace_model.py)
# Import necessary libraries
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import nltk
from nltk.corpus import stopwords
import numpy as np
from numpy.linalg import norm

# Define the training and test sets of text documents
train_set = ["The sky is blue.", "The sun is bright."]  # Documents
test_set = ["The sun in the sky is bright."]  # Query

# Get the stopwords for English language from NLTK
nltk.download('stopwords')
stopWords = stopwords.words('english')

# Initialize CountVectorizer and TfidfTransformer objects
vectorizer = CountVectorizer(stop_words=stopWords)
transformer = TfidfTransformer()

# Convert the training and test sets to arrays of TF-IDF features
trainVectorizerArray = vectorizer.fit_transform(train_set).toarray()
testVectorizerArray = vectorizer.transform(test_set).toarray()

# Display the TF-IDF arrays for training and test sets
print('Fit Vectorizer to train set:\n', trainVectorizerArray)
print('Transform Vectorizer to test set:\n', testVectorizerArray)

# Define a lambda function to calculate cosine similarity between vectors
cx = lambda a, b: round(np.inner(a, b) / (norm(a) * norm(b)), 3)

# Iterate through each vector in the training set
for vector in trainVectorizerArray:
    print("\nTrain Vector:", vector)
    # Iterate through each vector in the test set
    for testV in testVectorizerArray:
        print("Test Vector:", testV)
        cosine = cx(vector, testV)
        print("Cosine Similarity:", cosine)

# Fit the transformer to the training set and transform it to TF-IDF representation
transformer.fit(trainVectorizerArray)
print("\nTF-IDF representation of training set:")
print(transformer.transform(trainVectorizerArray).toarray())

# Fit the transformer to the test set and transform it to TF-IDF representation
transformer.fit(testVectorizerArray)
tfidf = transformer.transform(testVectorizerArray)
print("\nTF-IDF representation of test set:")
print(tfidf.todense())
print("Performed by Joshua Thadi 48")