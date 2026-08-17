# Email Spam Detection

## Overview
Binary classification model to detect spam vs. legitimate (ham) emails, comparing classical machine learning approaches against a fine-tuned transformer model. Built as part of the Oasis Infobyte Data Science internship (Task 4).

## Dataset
SMS Spam Collection dataset — 5,169 messages after deduplication (4,516 ham, 653 spam — a 87.4% / 12.6% class imbalance).

## Approach
1. Data cleaning: removed duplicates, checked nulls
2. EDA: class distribution, message length and word count by class
3. Text preprocessing: lowercasing, digit/punctuation removal, stopword removal
4. TF-IDF vectorization for classical models
5. Trained and compared 3 classical models: Naive Bayes, Logistic Regression (class-balanced), and SVM (GridSearchCV-tuned, class-balanced)
6. Fine-tuned DistilBERT (transformer-based) using Hugging Face `Trainer`, tokenizing raw messages directly
7. Compared all models on accuracy, precision, recall, and F1-score

## Key Findings
- Class imbalance (12.6% spam) made **recall** an important metric alongside accuracy — Naive Bayes and SVM had high precision but caught only ~72-74% of actual spam, meaning roughly 1 in 4 spam messages would slip through
- Logistic Regression improved recall (90.1%) at a moderate precision cost, a better trade-off for a spam filter than NB/SVM
- **Fine-tuned DistilBERT outperformed every classical model across all four metrics**, catching 96.9% of spam while maintaining 100% precision (zero false positives on the test set)

## Results

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| **DistilBERT** | **99.61%** | **100.00%** | **96.92%** | **98.44%** |
| Logistic Regression | 97.10% | 87.41% | 90.08% | 88.72% |
| Naive Bayes | 96.62% | 98.98% | 74.05% | 84.72% |
| Tuned SVM | 96.32% | 97.94% | 72.52% | 83.33% |

**Final model: DistilBERT (fine-tuned)** — highest performance across every metric, with a strong balance between catching spam and avoiding false positives.

## Tools Used
Python, pandas, scikit-learn, NLTK, PyTorch, Hugging Face Transformers & Datasets, joblib

## Files
- `EMAIL-SPAM.ipynb` — full notebook (EDA, preprocessing, classical models, DistilBERT fine-tuning, model comparison)
- `SPAM_BERT_MODEL/` — saved fine-tuned
