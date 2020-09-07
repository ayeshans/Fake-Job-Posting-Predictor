import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer

def text_tokenizer(text):
  if not (text == "" or pd.isnull(text)): 
    text = re.sub(r'URL_[A-Za-z0-9]+', ' ', text)
    return re.sub(r'[^A-Za-z0-9]+', ' ', text).lower().strip()


def get_model_input(text_input, vectorizer):
	text_input = text_tokenizer(text_input)
	return vectorizer.transform([text_input])