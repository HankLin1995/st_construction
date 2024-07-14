import streamlit as st

st.subheader(":black_nib: 工程基本資料")

with st.form("project_form"):

    project_name = st.text_input("🚧 工程名稱")
    project_place = st.text_input("📍 工程地點")
    project_contractor = st.text_input("🔧 承攬廠商")
    project_supervisor = st.text_input("🏢 主管機關")

    st.markdown("---")

    project_contract_number = st.text_input("📑 契約編號")
    project_contract_cost = st.text_input("💰 契約金額")

    st.markdown("---")

    project_start_date = st.date_input("🚀 開工日期")
    project_finish_date = st.date_input("🎯 預定完工日期")

    st.form_submit_button("送出")

    
