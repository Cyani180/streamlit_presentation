

import pandas as pd
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("MovieReview.csv")
st.dataframe(df.head(10))
st.write(df.shape)
st.dataframe(df.describe())

df = df.drop('sentiment', axis=1)























"""import streamlit as st
import random
import pickle
@st.cache_data
def generate_random_value(x): 
  return random.uniform(0, x) 
a = generate_random_value(10) 
b = generate_random_value(20) 
st.write(a) 
st.write(b)


loaded_model = pickle.load(open("model", 'rb'))"""
