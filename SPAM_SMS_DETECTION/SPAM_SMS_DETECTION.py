# AUTHOR: ABHIRAM R
# TASK NAME: SPAM SMS DETECTION
# TASK CATEGORY: MACHINE LEARNING
# GITHUB REPOSITORY: https://github.com/rAbhiram-github/MACHINE_LEARNING_PROJECTS/tree/main/SPAM_SMS_DETECTION



#  Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, f1_score, confusion_matrix
from sklearn.naive_bayes import MultinomialNB

#  Loading and Preprocessing Data
data = pd.read_csv('spam.csv',encoding = 'ISO-8859-1')
data = data.drop(columns=data.columns[2:5])
data.columns = ['Category', 'Message']

# Exploratory Data Analysis (EDA)
category_counts = data['Category'].value_counts().reset_index()
category_counts.columns = ['Category', 'Count']

# Creating Target Variable
data['spam']= data['Category'].apply(lambda x: 1 if x=='spam' else 0)

# Splitting Data
X_train, X_test, y_train, y_test = train_test_split(data.Message,data.spam, test_size=0.2)

from sklearn.feature_extraction.text import CountVectorizer

# Feature Extraction
featurer = CountVectorizer()
X_train_count = featurer.fit_transform(X_train.values)

# Training Naive Bayes Model
model = MultinomialNB()
model.fit(X_train_count,y_train)

#  Transforming Test Data
X_test_count = featurer.transform(X_test)

# Creating a Pipeline
from sklearn.pipeline import Pipeline
clf = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('nb', MultinomialNB())
])
clf.fit(X_train, y_train)

# Pre-trained model
pretrained_model = model 
new_sentences = [
    "Your account have 100 debeted, is waiting to be collected. Simply text the password \MIX\" to 85069 to verify. Get Usher and Britney. FML"
]
new_sentences_count = featurer.transform(new_sentences)

# Prediction
predictions = pretrained_model.predict(new_sentences_count)

for sentence, prediction in zip(new_sentences, predictions):
    if prediction == 1:
        print(f"'{sentence}' is a spam message.")
    else:
        print(f"'{sentence}' is not a spam message.")
