import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MostFrequentBaseline:

  def __init__(self, k=25):
    self.k = k
    self.top_k_ids = []

  def fit(self, train_df, target_col="MisconceptionId"):
    self.top_k_ids = (
        train_df[target_col].value_counts().head(self.k).index.tolist()
    )
    return self

  def predict(self, df):
    return [self.top_k_ids for _ in range(len(df))]


class TextSimilarityBaseline:

  def __init__(self, method="tfidf", k=25):
    self.method = method
    self.k = k
    if method == "tfidf":
      self.vectorizer = TfidfVectorizer(
          stop_words="english", ngram_range=(1, 2)
      )
    else:
      self.vectorizer = CountVectorizer(
          stop_words="english", ngram_range=(1, 2)
      )
    self.misconception_vectors = None
    self.misconception_ids = None

  def _prepare_text(self, df):
    if "full_text" in df.columns:
      return df["full_text"].fillna("").astype(str)
    cols = [
        c
        for c in [
            "SubjectName",
            "ConstructName",
            "QuestionText",
            "DistractorText",
        ]
        if c in df.columns
    ]
    return df[cols].fillna("").astype(str).agg(" ".join, axis=1)

  def fit(self, mapping_df):
    self.misconception_ids = mapping_df["MisconceptionId"].to_numpy()
    texts = mapping_df["MisconceptionName"].fillna("").astype(str)
    self.misconception_vectors = self.vectorizer.fit_transform(texts)
    return self

  def predict(self, df):
    query_texts = self._prepare_text(df)
    query_vectors = self.vectorizer.transform(query_texts)
    sim_matrix = cosine_similarity(query_vectors, self.misconception_vectors)
    top_k_indices = np.argsort(-sim_matrix, axis=1)[:, : self.k]
    return self.misconception_ids[top_k_indices].tolist()
