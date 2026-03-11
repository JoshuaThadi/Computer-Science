# document indexing and retrieval

import nltk
from nltk.corpus import stopwords

document1 = "The quick brown fox jumped over the lazy dog"
document2 = "The lazy dog slept in the sun"

nltk.download('stopwords')
stopwords = stopwords.words('english')

tokens1 = document1.lower().split()
tokens2 = document2.lower().split()

terms = list(set(tokens1 + tokens2))

inverted_index = {}
occ_num_doc1 = {}
occ_num_doc2 = {}

for term in terms:
    if term in stopwords:
        continue
    documents = []
    if term in tokens1:
        documents.append("Document 1")
        occ_num_doc1[term] = tokens1.count(term)
    if term in tokens2:
        documents.append("Document 2")
        occ_num_doc2[term] = tokens2.count(term)
    inverted_index[term] = documents

print("\n========= Inverted Index ==========\n")
for term, documents in inverted_index.items():
    print(term, "->", end="")
    for doc in documents:
        if doc == "Documents 1":
            print(f"{doc} ({occ_num_doc1.get(term, 0)}),", end="")
        else:
            print(f"{doc} ({occ_num_doc2.get(term, 0)})", end="")
    print()
