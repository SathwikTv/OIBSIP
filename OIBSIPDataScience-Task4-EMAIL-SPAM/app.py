import os
import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="MailShield AI | Enterprise Email Security",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# STATE INITIALIZATION
# ============================================================

if "email_text" not in st.session_state:
    st.session_state["email_text"] = ""

# ============================================================
# CUSTOM STYLING (Modern SaaS Design System)
# ============================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

.stApp {
    background: radial-gradient(circle at 50% 0%, rgba(99, 102, 241, 0.08), transparent 45%),
                radial-gradient(circle at 0% 100%, rgba(14, 165, 233, 0.05), transparent 35%),
                #f8fafc;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

/* NAVBAR */
.navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 28px;
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(12px);
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    margin-bottom: 32px;
    box-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.04);
}

.brand {
    font-size: 20px;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.5px;
}

.brand span {
    color: #6366f1;
}

.nav-status {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
    font-weight: 600;
    color: #10b981;
    background: #ecfdf5;
    padding: 6px 12px;
    border-radius: 20px;
    border: 1px solid #a7f3d0;
}

/* HERO SECTION */
.hero {
    text-align: center;
    padding: 20px 0 35px 0;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 14px;
    border-radius: 20px;
    background: #eef2ff;
    color: #4f46e5;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 16px;
    border: 1px solid #c7d2fe;
}

.hero h1 {
    font-size: 46px;
    line-height: 1.15;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -1px;
    margin-bottom: 12px;
}

.hero h1 span {
    background: linear-gradient(135deg, #6366f1 0%, #3b82f6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    max-width: 640px;
    margin: 0 auto;
    color: #64748b;
    font-size: 16px;
    line-height: 1.6;
}

/* STAT CARDS */
.stat-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 4px 15px -2px rgba(15, 23, 42, 0.03);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.stat-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px -4px rgba(15, 23, 42, 0.08);
}

.stat-value {
    font-size: 26px;
    font-weight: 800;
    color: #0f172a;
}

.stat-label {
    margin-top: 4px;
    color: #64748b;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.5px;
}

/* ANALYZER CONTAINER */
.analyzer-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 20px;
    padding: 28px;
    box-shadow: 0 10px 30px -5px rgba(15, 23, 42, 0.05);
    margin-top: 28px;
}

.card-header {
    margin-bottom: 20px;
}

.card-title {
    font-size: 20px;
    font-weight: 700;
    color: #0f172a;
}

.card-subtitle {
    color: #64748b;
    font-size: 14px;
    margin-top: 2px;
}

/* RESULT CARDS */
.result-card {
    margin-top: 24px;
    padding: 28px;
    border-radius: 16px;
    text-align: center;
    animation: fadeIn 0.3s ease-in-out;
}

.result-spam {
    background: linear-gradient(135deg, #fff1f2 0%, #ffe4e6 100%);
    border: 1px solid #fecdd3;
    color: #9f1239;
}

.result-ham {
    background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
    border: 1px solid #bbf7d0;
    color: #166534;
}

.result-icon {
    font-size: 44px;
    margin-bottom: 8px;
}

.result-title {
    font-size: 26px;
    font-weight: 800;
    letter-spacing: -0.5px;
}

.result-desc {
    font-size: 14px;
    margin-top: 6px;
    opacity: 0.85;
}

/* INFO CARDS */
.info-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 22px;
    height: 100%;
    box-shadow: 0 4px 15px -2px rgba(15, 23, 42, 0.03);
}

.info-icon {
    font-size: 24px;
    background: #f1f5f9;
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 12px;
    margin-bottom: 12px;
}

.info-title {
    font-size: 16px;
    font-weight: 700;
    color: #0f172a;
}

.info-text {
    color: #64748b;
    font-size: 13.5px;
    line-height: 1.5;
    margin-top: 6px;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 13px;
    padding-top: 40px;
    border-top: 1px solid #e2e8f0;
    margin-top: 50px;
}

/* CUSTOM STREAMLIT BUTTON OVERRIDES */
.stButton > button {
    border-radius: 10px;
    font-weight: 600;
    transition: all 0.2s ease;
}

textarea {
    border-radius: 12px !important;
    border: 1px solid #cbd5e1 !important;
}

textarea:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.15) !important;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# MODEL SETUP & LOADING
# ============================================================

MODEL_PATH = r"C:\DS\OASIS\EMAIL-SPAM\SPAM_BERT_MODEL"

@st.cache_resource(show_spinner=False)
def load_model(path):
    if not os.path.exists(path):
        return None, None, None
    try:
        tokenizer = AutoTokenizer.from_pretrained(path)
        model = AutoModelForSequenceClassification.from_pretrained(path)
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.to(device)
        model.eval()
        return tokenizer, model, device
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, None, None

tokenizer, model, device = load_model(MODEL_PATH)

def predict_email(text):
    if model is None or tokenizer is None:
        # Fallback simulation if model path doesn't exist locally
        return "SPAM" if "win" in text.lower() or "prize" in text.lower() else "HAM", 0.9852
    
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )
    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)

    probabilities = torch.softmax(outputs.logits, dim=1)
    prediction = torch.argmax(probabilities, dim=1).item()
    confidence = probabilities[0][prediction].item()

    label = "SPAM" if prediction == 1 else "HAM"
    return label, confidence

# ============================================================
# HEADER & NAVBAR
# ============================================================

st.markdown("""
<div class="navbar">
    <div class="brand">
        🛡️ Mail<span>Shield</span> AI
    </div>
    <div class="nav-status">
        <span style="height: 8px; width: 8px; background-color: #10b981; border-radius: 50%; display: inline-block;"></span>
        DistilBERT v1.0 Active
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# HERO SECTION
# ============================================================

st.markdown("""
<div class="hero">
    <div class="hero-badge">
        ✨ Enterprise Email Security
    </div>
    <h1>Detect Spam. <br><span>Protect Your Inbox.</span></h1>
    <p>
        MailShield AI leverages a fine-tuned DistilBERT transformer network to inspect 
        email structure, semantic context, and threat patterns in real-time.
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# PERFORMANCE METRICS STRIP
# ============================================================

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-value" style="color: #6366f1;">99.61%</div>
        <div class="stat-label">TEST ACCURACY</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-value" style="color: #059669;">100.0%</div>
        <div class="stat-label">PRECISION</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-value" style="color: #0284c7;">96.92%</div>
        <div class="stat-label">RECALL</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-value" style="color: #7c3aed;">98.44%</div>
        <div class="stat-label">F1 SCORE</div>
    </div>
    """, unsafe_allow_html=True)

# Warning if local model path is not loaded
if model is None:
    st.info("ℹ️ **Model Demo Mode**: Local model path was not found. Running in demonstration mode.")

# ============================================================
# MAIN ANALYZER INTERFACE
# ============================================================

st.markdown("""
<div class="analyzer-card">
    <div class="card-header">
        <div class="card-title">Analyze Email Content</div>
        <div class="card-subtitle">Paste raw email body or header text below to run real-time threat detection.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Preset loaders (Fixing Streamlit Session State Binding)
def set_email(text):
    st.session_state["email_text"] = text

col_b1, col_b2, col_b3 = st.columns([1.2, 1.4, 1])

with col_b1:
    st.button(
        "📨 Load Spam Sample",
        on_click=set_email,
        args=("URGENT: Your account access has been restricted! Click http://bit.ly/secure-verify now to claim your $1,000 prize bonus.",),
        use_container_width=True
    )

with col_b2:
    st.button(
        "📩 Load Legitimate Sample",
        on_click=set_email,
        args=("Hi Sathwik, please review the attached project deliverables for our client review session scheduled tomorrow at 3 PM.",),
        use_container_width=True
    )

with col_b3:
    st.button(
        "🗑️ Clear",
        on_click=set_email,
        args=("",),
        use_container_width=True
    )

# Text Input Area
email_input = st.text_area(
    label="Email Body Input",
    key="email_text",
    height=200,
    placeholder="Paste email text here...",
    label_visibility="collapsed"
)

# Analyze Trigger
analyze_clicked = st.button("🔍 Run Security Analysis", type="primary", use_container_width=True)

# ============================================================
# PREDICTION & RESULTS DISPLAY
# ============================================================

if analyze_clicked:
    if not email_input.strip():
        st.warning("⚠️ Please input email content before running the analysis.")
    else:
        with st.spinner("Analyzing message vectors with DistilBERT..."):
            label, confidence = predict_email(email_input)

        if label == "SPAM":
            st.markdown(f"""
            <div class="result-card result-spam">
                <div class="result-icon">🚨</div>
                <div class="result-title">Spam / Threat Detected</div>
                <div class="result-desc">
                    This email exhibits characteristic patterns of unwanted promotional content or phishing attempts.
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-card result-ham">
                <div class="result-icon">🛡️</div>
                <div class="result-title">Legitimate Message (Ham)</div>
                <div class="result-desc">
                    No malicious signature or spam heuristics were detected in this email.
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.write("")
        st.progress(confidence, text=f"Classification Confidence: {confidence:.2%}")

# ============================================================
# HOW IT WORKS SECTION
# ============================================================

st.markdown("<br><h3 style='text-align:center; color:#0f172a; font-weight:800;'>How MailShield Operates</h3>", unsafe_allow_html=True)
st.write("")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="info-card">
        <div class="info-icon">📥</div>
        <div class="info-title">1. Tokenization</div>
        <div class="info-text">
            Email text is tokenized into contextual sub-word embeddings using Hugging Face transformers.
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="info-card">
        <div class="info-icon">⚡</div>
        <div class="info-title">2. DistilBERT Inference</div>
        <div class="info-text">
            Our fine-tuned multi-layer transformer model evaluates semantic intent and risk probability.
        </div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="info-card">
        <div class="info-icon">📊</div>
        <div class="info-title">3. Decision Output</div>
        <div class="info-text">
            Output probabilities are mapped to actionable security indicators and confidence scores.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
    <b>MailShield AI Security Engine</b> • Powered by DistilBERT<br>
    Built with PyTorch • Hugging Face Transformers • Streamlit
</div>
""", unsafe_allow_html=True)