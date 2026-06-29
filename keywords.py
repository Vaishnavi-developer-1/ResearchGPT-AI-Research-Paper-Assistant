import spacy
import nltk
from nltk.corpus import stopwords
from collections import Counter

nltk.download('stopwords')
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text, top_n=10):
    stop_words = set(stopwords.words('english'))
    doc = nlp(text.lower())
    words = [
        token.lemma_ for token in doc
        if token.is_alpha and token.text not in stop_words and len(token.text) > 3
    ]
    return [word for word, _ in Counter(words).most_common(top_n)]

def extract_topics(text):
    doc = nlp(text)
    topics = list(set([ent.text for ent in doc.ents if ent.label_ in ["ORG", "GPE", "PRODUCT", "WORK_OF_ART"]]))
    return topics[:10]