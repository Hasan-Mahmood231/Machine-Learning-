import streamlit as st

st.title("Hellow guys")
st.subheader("Select your fav language.")
lang = st.selectbox("My fav language is ",['cpp','python','java','R','skala'])
st.write(f"Your fav language is {lang}")
st.success("your language is really great")