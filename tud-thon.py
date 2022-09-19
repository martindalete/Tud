import pandas as pd
import streamlit as st
import random

st.experimental_memo.clear()
st.set_page_config(page_title="Tud is")

nouns = pd.read_csv(r"https://raw.githubusercontent.com/martindalete/Tud/main/91Knouns.txt", header = None, names = ['Noun'])
adverbs = pd.read_csv(r"https://raw.githubusercontent.com/martindalete/Tud/main/6Kadverbs.txt", header = None, names = ['Adverb'])
adjectives = pd.read_csv(r"https://raw.githubusercontent.com/martindalete/Tud/main/28Kadjectives.txt", header = None, names = ['Adjective'])

def display_button():
    st.button('What is Tud?')
    st.write('Tud is a ' + adverbs.iloc[random.randint(0,len(adverbs))]['Adverb'] + \
           ' ' + \
           adjectives.iloc[random.randint(0,len(adjectives))]['Adjective'] + \
           ' ' + \
           nouns.iloc[random.randint(0,len(nouns))]['Noun'] + \
           '.')
display_button()
