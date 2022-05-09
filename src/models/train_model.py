from sklearn.feature_extraction.text import CountVectorizer

def vectorizer(df):
    cm = CountVectorizer().fit_transform(df.Tags)
    return cosine_similarity(cm)