import streamlit as st
import pandas as pd


st.set_page_config(layout= "wide")


df_reviews = pd.read_csv("customer_reviews.csv")
df_top100_books = pd.read_csv("Top-100_Books.csv")

# lista contendo nomes dos livros individuais
books = df_top100_books['book title'].unique()

book = st.sidebar.selectbox('books', books)

df_book= df_top100_books[df_top100_books['book title'] == book]
df_reviewsf= df_reviews[df_reviews['book name'] == book]

#pega so o titulo...
book_title = df_book['book title'].iloc[0]
book_genre = df_book['genre'].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_rating = df_book['rating'].iloc[0]
book_year = df_book['year of publication'].iloc[0]

st.title(book_title)
st.subheader(book_genre)

#define 3 variaveis
col1, col2, col3 = st.columns(3)
col1.metric('Price', book_price)
col2.metric('Rating', book_rating)
col3.metric('Year of publication', book_year)

#linha 
st.divider()

df_reviewsf
for row in df_reviewsf.values:
    message = st.chat_message(f'{row[4]}')
    message.write(f'**{row[2]}**')
    message.write(row[5])



# df_book
# df_reviewsf
