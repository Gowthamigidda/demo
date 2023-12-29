import streamlit as st
st.set_page_config(page_title='cats')
st.header("Types of Cats")
c1,c2=st.columns(2)
with c1:
  st.write("-White Cat")
  st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F321022279681136618%2F&psig=AOvVaw0TTxj90QEVqYxJgl46Ki9r&ust=1703917451388000&source=images&cd=vfe&ved=0CBIQjRxqFwoTCKjdmp2FtIMDFQAAAAAdAAAAABAE",width=600,use_column_width=True)
with c2:
  st.write("-Persian Cat")
  st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSt8T7X9bO9-L1tUZw-C-PwSSD973LYAxcYaF4dqykXW2HmOx9aMKuRlhP-0Q&s",width=600,use_column_width=True)
