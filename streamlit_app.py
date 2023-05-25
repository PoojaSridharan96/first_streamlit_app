import streamlit
streamlit.title('MY PARENTS NEW HEALTHY DINER')
streamlit.header('BREAKFAST MENU')
streamlit.text('🥗 American Breakfast')
streamlit.text('🐔 Hard boiled free range egg')
streamlit.text('🥣 Kale,Spinach & Rocket Smoothie')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list=pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(my_fruit_list)
