import streamlit as st
import joblib
import requests
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Load your ML model and vectorizer
clf = joblib.load("models/logistic_regression_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Ensure NLTK resources are available
def safe_nltk_download(resource):
    try:
        nltk.data.find(resource)
    except LookupError:
        nltk.download(resource.split('/')[-1])

safe_nltk_download('tokenizers/punkt')
safe_nltk_download('corpora/stopwords')
safe_nltk_download('corpora/wordnet')
safe_nltk_download('corpora/omw-1.4')

# Preprocessing function
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = text.split()
    cleaned = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return ' '.join(cleaned)

# Google Fact Check API function
def google_fact_check(query, api_key):
    url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
    params = {
        "query": query,
        "key": api_key,
        "languageCode": "en"
    }
    response = requests.get(url, params=params)
    return response.json()

API_KEY = "AIzaSyAaBqHBNLz60JENBCjKXF8zQ3xyIe-W-7o"

st.title("Rumour Detection & Fact Check")

user_input = st.text_area("Enter a statement to check:")

if st.button("Check"):
    # ML Prediction
    clean = preprocess_text(user_input)
    vec = vectorizer.transform([clean])
    prediction = clf.predict(vec)[0]
    st.write(f"**ML Model Prediction:** {prediction}")

    # Google Fact Check
    result = google_fact_check(user_input, API_KEY)
    claims = result.get("claims", [])
    if not claims:
        st.write("No fact-check found for your statement.")
    else:
        for claim in claims:
            st.write(f"**Claim found:** {claim.get('text')}")
            st.write(f"**Claimed by:** {claim.get('claimant')}")
            review = claim.get("claimReview", [{}])[0]
            st.write(f"**Rating:** {review.get('textualRating')}")
            st.write(f"[More info]({review.get('url')})")
            st.write("---")