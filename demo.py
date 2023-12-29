import streamlit as st
st.set_page_config(page_title='cats')
st.header("Types of Cats")
c1,c2=st.columns(2)
with c1:
  st.write("-White Cat")
  st.image("https://i.pinimg.com/originals/3e/f9/b8/3ef9b84d91827bc0f9bc94dea55eac90.jpg",width=600,use_column_width=True)
with c2:
  st.write("-Persian Cat")
  st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSt8T7X9bO9-L1tUZw-C-PwSSD973LYAxcYaF4dqykXW2HmOx9aMKuRlhP-0Q&s",width=600,use_column_width=True)
