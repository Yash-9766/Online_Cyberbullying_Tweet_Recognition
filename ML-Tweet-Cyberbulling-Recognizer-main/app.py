import pandas as pd
import streamlit as st
from PIL import Image
import numpy as np
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import PorterStemmer, WordNetLemmatizer
from Prediction import *
import pickle

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('omw-1.4')

# Page title
st.set_page_config(page_title="Twitter Sentiment Explorer", page_icon=Image.open('statics/mit.png'),initial_sidebar_state="expanded")

# Add profile image
profile_image = Image.open("statics/mit.png")
st.sidebar.image(profile_image, use_column_width=True)

# Add contact information
st.sidebar.title("TEAM MEMBERS :- ")
st.sidebar.write("Abhijeet Sawant - T228005")
st.sidebar.subheader("Roll No = 178")
st.sidebar.subheader("abhijeet.sawant@mitaoe.ac.in")

st.sidebar.write("Yash Gaikwad - T228041")
st.sidebar.subheader("Roll No = 182")
st.sidebar.subheader("yash.gaikwad@mitaoe.ac.in")

st.sidebar.write("Tejas Jadhav - T228054")
st.sidebar.subheader("Roll No  = 184")
st.sidebar.subheader("tejas.jadhav@mitaoe.ac.in")


st.write('''
# Cyberbullying Tweet Recognition App

This app predicts the nature of the tweet into 6 Categories.
* Age
* Ethnicity
* Gender
* Religion
* Other Cyberbullying
* Not Cyberbullying

***
''')

image = Image.open('statics/twitter.png')
st.image(image, use_column_width= True)

# Text Box
st.header('Enter Tweet ')
tweet_input = st.text_area("Tweet Input", height= 150)
print(tweet_input)
st.write('''
***
''')

# print input on webpage
if tweet_input:
    st.header('''
    ***Predicting......
    ''')
else:
    st.write('''
    ***No Tweet Text Entered!***
    ''')
st.write('''
***
''')

# Output on the page
st.header("Prediction")
if tweet_input:
    prediction = prediction(tweet_input)
    if prediction == "age":
        st.image("statics/Age.png",use_column_width= True)
    elif prediction == "ethnicity":
        st.image("statics/Ethnicity.png",use_column_width= True)
    elif prediction == "gender":
        st.image("statics/Gender.png",use_column_width= True)
    elif prediction == "other_cyberbullying":
        st.image("statics/Other.png",use_column_width= True)
    elif prediction == "religion":
        st.image("statics/Religion.png",use_column_width= True)
    elif prediction == "not_cyberbullying":
        st.image("statics/not_cyber.png",use_column_width= True)
else:
    st.write('''
    ***No Text Entered!***
    ''')

st.write('''***''')
