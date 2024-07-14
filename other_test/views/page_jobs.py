import streamlit as st
import pandas as pd
from datetime import datetime

user_id=st.session_state.user_id
st.sidebar.write(f":male-firefighter: 使用者:**{user_id}**")


def get_fixed_projects():
    data = {
        "工程編號": ["P001", "P002", "P003", "P004", "P005"],
        "工程名稱": ["Bridge Construction", "Road Expansion", "Water Treatment Plant", "Airport Renovation", "Subway Extension"],
        "建立日期": [
            datetime(2023, 1, 15), 
            datetime(2023, 3, 22), 
            datetime(2023, 5, 10), 
            datetime(2023, 7, 1), 
            datetime(2023, 8, 25)
        ],
        "擔任角色": ["工地主任", "現場工程師", "品管人員", "職安人員","監造人員" ],
        "狀態": ["Planning", "In Progress", "Completed", "On Hold", "Cancelled"]
    }
    
    return pd.DataFrame(data)

st.subheader("工程專案內容")

fixed_projects_df = get_fixed_projects()

st.write(fixed_projects_df)
