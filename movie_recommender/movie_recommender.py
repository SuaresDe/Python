import pandas as pd
import numpy as np
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.neighbors import NearestNeighbors

df = pd.read_csv("movie_dataset.csv", low_memory=False)

df = df[["original_title", "overview", "tagline", "genres", "keywords"]].dropna()

def process_column(text):
    try:
        items = ast.literal_eval(text)  
        return " ".join([item["name"] for item in items])  
    except:
        return ""  

df["genres"] = df["genres"].apply(process_column)
df["keywords"] = df["keywords"].apply(process_column)

df["content"] = df["overview"] + " " + df["tagline"] + " " + df["genres"] + " " + df["keywords"]

tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["content"])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)  

index = pd.Series(df.index, index=df["original_title"]).drop_duplicates()

nn_model = NearestNeighbors(metric="cosine", algorithm="brute", n_neighbors=10)
nn_model.fit(tfidf_matrix)

def recommend_movies(title, n_recommendations=10):
    if title not in index:
        return f"❌ Movie '{title}' not found! Try again."

    idx = index[title]

    if isinstance(idx, pd.Series):
        idx = idx.iloc[0]  

    if idx >= tfidf_matrix.shape[0] or idx < 0:
        return f"⚠️ Invalid index for '{title}'. Try another movie."

    distances, indices = nn_model.kneighbors(tfidf_matrix[idx], n_neighbors=n_recommendations+1)

    recommendations = [df["original_title"].iloc[i] for i in indices.flatten()[1:]]
    
    return recommendations

while True:
    movie = input("\n Enter a movie name (or type 'exit' to quit): ").strip()
    
    if movie.lower() == "exit":
        print(" Exiting movie recommendation system. Goodbye!")
        break  

    recommendations = recommend_movies(movie)

    if isinstance(recommendations, list):
        print("\n Recommended Movies:")
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec}")
    else:
        print(recommendations)  


        print("\n Did you mean one of these?")
        print(df["original_title"].sample(10).to_string(index=False)) 