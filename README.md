# 🕵️‍♂️ Rumour Detection System (Fake News Classifier)

A Machine Learning-based web app that detects **rumours** or **fake news** from textual statements using **Logistic Regression with TF-IDF**, along with real-time validation using the **Google Fact Check API**.

---

## 📌 Features

- ✅ Detects if a given statement is a **rumour** or **real**
- 📊 Trained using a labelled dataset with **TF-IDF vectorization**
- 🧠 Machine Learning Model: **Logistic Regression**
- 🔍 Performs **text preprocessing**: tokenization, stopword removal, lemmatization
- 🔗 Uses **Google Fact Check API** for trusted verification
- 🌐 Web UI built using **Streamlit**

---

## 🗃️ Dataset

The dataset includes three TSV files:
- `train.tsv`
- `valid.tsv`
- `test.tsv`

Each entry includes:
- Statement text
- Label (true/false/half-true/etc.)
- Speaker info
- Subject, party affiliation, and more

---

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/rumour-detection.git
cd rumour-detection



Install requirements
pip install -r requirements.txt



Download NLTK dependencies (optional if not auto-downloaded)
python nltk_setup.py


🚀 Run the App
streamlit run app.py
Then open your browser at: http://localhost:8501

8501

🧪 Model & Preprocessing
Model: Logistic Regression (scikit-learn)

Vectorizer: TF-IDF

Preprocessing:

Lowercasing

Removing special characters

Tokenization

Stopword removal (nltk.corpus.stopwords)

Lemmatization (WordNetLemmatizer)

Model and vectorizer are stored in /models as:

logistic_regression_model.pkl

tfidf_vectorizer.pkl

Google Fact Check API
Integrates Google Fact Check Tools API

Checks real-world claims related to the input

Requires a valid Google API Key




📈 Future Scope
Add GNN-based rumour detection from tweet propagation

Improve model with deep learning (e.g. BERT)

Support for multilingual datasets

Add Twitter/X API integration for live data


📚 References
scikit-learn

NLTK

Streamlit

Google Fact Check API


👤 Author
Akshat Sharma
Email: Asharmabwn123@gmail.com




