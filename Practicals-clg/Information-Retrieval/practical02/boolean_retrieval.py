# Aim: Retrieval Models
# ● Implement the Boolean retrieval model and process queries.
# ● Implement the vector space model with TF-IDF weighting and cosine similarity. 

# Part-1 (Boolean-retrieval.py)
documents = {
    1: "apple banana orange",
    2: "apple banana",
    3: "banana orange",
    4: "apple"
}

# Function to build an inverted index using dictionaries
def build_index(docs):
    index = {}
    for doc_id, text in docs.items():
        terms = set(text.split())
        for term in terms:
            if term not in index:
                index[term] = {doc_id}
            else:
                index[term].add(doc_id)
    return index

# Building the inverted index
inverted_index = build_index(documents)

# Function for Boolean AND operation using inverted index
def boolean_and(operands, index, all_doc_keys):
    if not operands:
        # Return all document IDs if query is empty
        return list(all_doc_keys)

    # Get the set of document IDs for the first operand, default to an empty set
    result = index.get(operands[0], set())

    for term in operands[1:]:
        # Compute intersection with sets of document IDs
        result = result.intersection(index.get(term, set()))
        # Optimization: If result is empty, stop early
        if not result:
            return []

    return list(result)

# Function for Boolean OR operation using inverted index
def boolean_or(operands, index):
    result = set()
    for term in operands:
        # Union of sets of document IDs for each term
        result = result.union(index.get(term, set()))
    return list(result)

# Function for Boolean NOT operation using inverted index
# Pass the original documents to correctly determine *all* possible IDs
def boolean_not(operand, index, documents):
    # Get the set of document IDs for the operand, default to empty set
    operand_set = index.get(operand, set())
    # Create a set of all valid document IDs from the documents dictionary
    all_docs_set = set(documents.keys())
    # Return documents not in the operand set
    return list(all_docs_set.difference(operand_set))

# --- Example queries ---
query1 = ["apple", "banana"]
query2 = ["apple", "orange"]

# Pass documents.keys() or documents to the modified functions
all_doc_keys = documents.keys()
result1 = boolean_and(query1, inverted_index, all_doc_keys)
result2 = boolean_or(query2, inverted_index)
result3 = boolean_not("orange", inverted_index, documents) # Using the improved NOT

print("Documents containing 'apple' and 'banana':", result1)
print("Documents containing 'apple' or 'orange':", result2)
print("Documents not containing 'orange':", result3)
print("---")
print("Performed by Joshua Thadi 48")