# pip install -U streamlit
# streamlit run app.py

import streamlit as st
import pickle

model = pickle.load(open('sentiment_analysis.pkl', 'rb'))

st.title('Cineotion: Movie Review Sentiment Analysis')

st.write('Enter a movie review below and click on the "Analyze Sentiment" button to see the sentiment (Positive/Negative) of the review.')

review = st.text_area('Enter your movie review here...')

submit = st.button('Analyze Sentiment')

if submit:
    prediction = model.predict([review])


    if prediction[0] == 'positive':
        st.success('Positive Review')
    else:
        st.warning('Negative Review')