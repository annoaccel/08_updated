import streamlit as st

from public.login import user

st.image("./logo.png")
st.title("Avistos Innovative Solutions")

st.header("Welcome To Profile-Page")
# st.write(f'Welcome *{user}*')
st.header(f'Welcome *{user}*')
