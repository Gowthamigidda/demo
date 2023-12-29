import streamlit as st
st.set_page_config(page_title='cats')
st.markdown("## Types of Cats")
st.write("-White Cat")
st.image("https://www.rover.com/blog/wp-content/uploads/white-cat-min.jpg",width=600)
st.write("-Persian Cat")
st.image("data:image/jpeg;base64,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",width=600)
