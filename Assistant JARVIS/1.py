import nltk
import spacy
import numpy as np
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from textblob import TextBlob
from gensim import corpora
from gensim.models import LdaModel, Word2Vec
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    return [word for word in tokens if word.isalnum() and word not in stop_words]

def analyze_text_nltk(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalnum()]
    filtered_words = [word for word in words if word not in stopwords.words('english')]
    freq_dist = FreqDist(filtered_words)
    blob = TextBlob(text)
    sentiment = blob.sentiment

    print("NLTK Analysis")
    print("Number of sentences:", len(sentences))
    print("Number of words:", len(words))
    print("Filtered words:", len(filtered_words))
    print("\nFrequency Distribution:")
    for word, freq in freq_dist.items():
        print(f"{word}: {freq}")
    print("\nSentiment Analysis:")
    print(f"Polarity: {sentiment.polarity}")
    print(f"Subjectivity: {sentiment.subjectivity}\n")

def analyze_text_spacy(text):
    doc = nlp(text)

    print("spaCy Analysis")
    print("Named Entities, Phrases, and Concepts:")
    for ent in doc.ents:
        print(f"{ent.text} ({ent.label_})")

    print("\nPart-of-Speech Tagging:")
    for token in doc:
        print(f"{token.text}: {token.pos_}")

    print("\nDependency Parsing:")
    for token in doc:
        print(f"{token.text} -> {token.dep_} -> {token.head.text}\n")

def topic_modeling(texts):
    processed_texts = [preprocess_text(text) for text in texts]
    dictionary = corpora.Dictionary(processed_texts)
    corpus = [dictionary.doc2bow(text) for text in processed_texts]
    lda_model = LdaModel(corpus, num_topics=2, id2word=dictionary, passes=15)

    print("Topic Modeling:")
    for idx, topic in lda_model.print_topics(-1):
        print(f"Topic: {idx}\nWords: {topic}\n")

def word_embeddings(texts):
    processed_texts = [preprocess_text(text) for text in texts]
    model = Word2Vec(sentences=processed_texts, vector_size=100, window=5, min_count=1, sg=0)

    print("Word Embeddings:")
    for word in model.wv.index_to_key:
        print(f"Word: {word}, Vector: {model.wv[word]}\n")

def text_classification(texts, labels):
    X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.3, random_state=42)
    model = make_pipeline(CountVectorizer(), MultinomialNB())
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    print(f"Text Classification Accuracy: {accuracy:.2f}")

def text_summarization(text):
    parser = PlaintextParser.from_string(text, tokenizer('english'))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, 2)  # Summarize to 2 sentences

    print("Text Summarization:")
    for sentence in summary:
        print(sentence)

def text_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    
    print(f"Text Similarity: {similarity[0][0]:.2f}")

if __name__ == "__main__":
    sample_text = """
    Apple Inc. is an American multinational technology company headquartered in Cupertino, California.
    It is one of the Big Tech companies, alongside Amazon, Google, Microsoft, and Facebook.
    """

    sample_texts = [
        "Apple is looking at buying U.K. startup for $1 billion.",
        "The technology sector is booming with new innovations.",
        "Microsoft announced new features for its Office suite.",
        "The health benefits of regular exercise are well-documented."
    ]
    labels = ["positive", "neutral", "positive", "negative"]

    print("Running text analysis...\n")
    analyze_text_nltk(sample_text)
    analyze_text_spacy(sample_text)
    topic_modeling(sample_texts)
    word_embeddings(sample_texts)
    text_classification(sample_texts, labels)
    text_summarization(sample_text)
    text_similarity(sample_text, sample_texts[0])
