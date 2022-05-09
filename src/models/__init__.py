import pandas as pd
import logging
from src.models.train_model import vectorizer

df = pd.read_csv('data/processed/data.csv')

cs = vectorizer(df)

print(cs)