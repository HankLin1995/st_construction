import streamlit as st

st.subheader("使用者登入")

with st.form("login"):

    user_id=st.text_input("帳號",value="HankLin")
    password=st.text_input("密碼",type="password")

    if st.form_submit_button("登入"):
        st.session_state.user_id="HankLin"
        st.success("OK!")
