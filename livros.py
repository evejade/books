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
df_books
#count valores de quantas aparições de cada ano e monta o histograma 
fig= px.bar(df_top100_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])
col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)

