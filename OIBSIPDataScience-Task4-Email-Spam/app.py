import streamlit as st
import joblib
import re
import string
import nltk
from nltk.corpus import stopwords

# ── Page config ────────────────────────────────────────────────
st.set_page_config(
    page_title="Email Spam Classifier",
    page_icon="📧",
    layout="centered"
)

# ── Load model artifacts (cached so they load once) ─────────────
@st.cache_resource
def load_artifacts():
    nltk.download('stopwords', quiet=True)
    model = joblib.load("spam_classifier_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")
    return model, vectorizer

model, tfidf = load_artifacts()
stop_words = set(stopwords.words('english'))

# ── Preprocessing (must match training pipeline exactly) ────────
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def remove_stopwords(text):
    return ' '.join([word for word in text.split() if word not in stop_words])

def predict_email(text):
    cleaned = clean_text(text)
    cleaned = remove_stopwords(cleaned)
    vec = tfidf.transform([cleaned])
    prediction = model.predict(vec)[0]
    score = model.decision_function(vec)[0]
    return prediction, score

# ── UI ────────────────────────────────────────────────────────
st.title("📧 Email Spam Classifier")
st.caption("SVM model trained on TF-IDF features — 97.7% test accuracy")

st.divider()

email_text = st.text_area(
    "Paste an email or message below:",
    height=200,
    placeholder="e.g. Congratulations! You've won a $1,000 prize. Click here to claim..."
)

col1, col2 = st.columns([1, 3])
with col1:
    classify_btn = st.button("Classify", type="primary", use_container_width=True)

if classify_btn:
    if not email_text.strip():
        st.warning("Please enter a message to classify.")
    else:
        prediction, score = predict_email(email_text)

        st.divider()

        if prediction == 1:
            st.error("🚨 **SPAM**")
        else:
            st.success("✅ **NOT SPAM (Ham)**")

        # Confidence score — LinearSVC has no predict_proba, so we show
        # decision_function distance instead (not a true probability).
        confidence = min(abs(score) / 3, 1.0) * 100  # rough normalization for display
        st.caption(f"Confidence score: {confidence:.1f}%  (distance from decision boundary: {score:.3f})")

        with st.expander("See cleaned text used for prediction"):
            cleaned_preview = remove_stopwords(clean_text(email_text))
            st.code(cleaned_preview if cleaned_preview else "(empty after cleaning)")

st.divider()
st.caption("Model: Linear SVM · Vectorizer: TF-IDF (5000 features, 1-2 grams) · Sathwik TV")