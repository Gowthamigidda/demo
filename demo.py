import streamlit as st
from PIL import Image
st.set_page_config(page_title='cats')
st.markdown("## Types of Cats")
st.write("-Persian Cat")
image = Image.open(r'C:\Users\Administrator\Downloads\perse.jpg')
st.image(image, caption='Enter any caption here')
st.write("-White Cat")

