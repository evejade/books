import streamlit as st
import pandas as pd
import plotly.express as px

#config da pag
st.set_page_config(
    #== height vh
    layout="wide"
    )

df_reviews =pd.read_csv("customer_reviews.csv")
df_top100_books= pd.read_csv("Top-100_Books.csv")

price_max = df_top100_books["book price"].max()
price_min= df_top100_books["book price"].min()

#define o slider
max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)
#"liga" o slider aos dados
df_books = df_top100_books[df_top100_books["book price"] <= max_price]


