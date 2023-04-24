# Import libraries
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import scipy.sparse as sp

# Function that takes in movie title as input and outputs most similar movies
def get_recommendations(user_input):

    # Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
    tfidf = TfidfVectorizer(stop_words='english')

     # Load database and construct the required TF-IDF matrix by fitting and transforming it
    metadata = pd.read_csv('../data/movies_metadata.csv', low_memory=False)
    metadata['overview'] = metadata['overview'].fillna('')
    tfidf_matrix = tfidf.fit_transform(metadata['overview'])

    # Construct the required TF-IDF matrix by transforming and reshaping the user input
    tfidf_user_input = tfidf.transform([user_input])
    sparse_matrix = sp.csr_matrix(tfidf_user_input)
    tfidf_user_input_matrix = sp.hstack([sparse_matrix, sp.csr_matrix((sparse_matrix.shape[0], tfidf_matrix.shape[1] - sparse_matrix.shape[1]))])

    # Compute the cosine similarity matrix between both matrixes
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_user_input_matrix)

    # Sort the movies based on the similarity scores
    sim_scores = np.argsort(cosine_sim.flatten())[::-1] 

    # Get the indexes of the 5 most similar movies
    movie_indices = sim_scores[:5]

    # Return the top 5 most similar movies
    return metadata[['title', 'overview']].iloc[movie_indices]