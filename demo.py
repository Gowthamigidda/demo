import streamlit as st
from PIL import Image
st.set_page_config(page_title='cats')
st.markdown("## Types of Cats")
st.write("-Persian Cat")
image = Image.open('./perse.jpg')
st.image(image)
st.write("-White Cat")
st.image("C:\Users\Administrator\Downloads\perse.jpg")

