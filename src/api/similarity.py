import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity as cosine_sim
from collections import Counter

def jaccard_similarity(str1, str2):
    # Tokenize the strings
    set1, set2 = set(str1.lower().split()), set(str2.lower().split())
    # Calculate intersection and union
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return float(intersection) / union if union != 0 else 0

def cosine_similarity(str1, str2):
    # Use CountVectorizer to create document-term matrices
    vectorizer = CountVectorizer().fit_transform([str1, str2])
    vectors = vectorizer.toarray()
    return cosine_sim(vectors)[0][1]