# Email Spam Detection with Machine Learning

## OASIS Infobyte Internship

**Intern:** Sathwik TV  
**Role:** Data Science Intern  
**Task:** Email Spam Detection with Machine Learning

## Project Overview

This project focuses on detecting whether a message is **spam** or **ham (legitimate)** using machine learning and natural language processing techniques.

The project was completed as part of my **OASIS Infobyte Data Science Internship**.

## Dataset

The project uses the SMS Spam Collection dataset.

- Original records: **5,572**
- Duplicate records removed: **403**
- Final records: **5,169**
- Ham messages: **4,516**
- Spam messages: **653**

The dataset contains two main columns:

- `label` — spam or ham
- `message` — the text message

## Data Preprocessing

The dataset was inspected for structure, missing values, and duplicate records. No missing values were found.

Duplicate records were removed, reducing the dataset from 5,572 to 5,169 records.

## Exploratory Data Analysis

Exploratory analysis was performed to understand the distribution of spam and ham messages.

The final dataset contains:

- **87.37% ham messages**
- **12.63% spam messages**

## Text Feature Extraction

Text messages were converted into numerical features using **TF-IDF (Term Frequency–Inverse Document Frequency)**.

TF-IDF was used to represent important words and word combinations in the messages for machine learning.

## Machine Learning

A **Linear Support Vector Classification (LinearSVC)** model was used for spam classification.

The model was trained using the TF-IDF text features and evaluated using classification metrics.

## Results

The final model achieved an accuracy of approximately:

**97.68%**

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF
- LinearSVC
- Matplotlib
- Seaborn

## Key Learning Outcomes

- Data cleaning and preprocessing
- Exploratory data analysis
- Text preprocessing and feature extraction
- TF-IDF vectorization
- Machine learning classification
- Model evaluation

## Internship

This project was completed as part of the **OASIS Infobyte Data Science Internship**.

**Task: Email Spam Detection with Machine Learning**
