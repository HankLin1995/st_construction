import streamlit as st
import pandas as pd
from datetime import datetime
from database import Project, get_session

# 初始化 session_state
if 'active_project_id' not in st.session_state:
    st.session_state['active_project_id'] = None
if 'active_project_name' not in st.session_state:
    st.session_state['active_project_name'] = None 

@st.experimental_dialog(title="📂 新增專案")
def add_project_form():
    new_project_name = st.text_input("專案名稱")
    new_project_description = st.text_input("專案描述")
    new_project_create_user = st.text_input("建立人員")
    new_project_create_time = datetime.now()

    if st.button("送出"):
        add_project(new_project_name, new_project_description,new_project_create_user,new_project_create_time)
        st.rerun()

@st.experimental_dialog(title="⚠️ 刪除專案")
def delete_project_form():
    new_project_id= st.text_input("刪除的專案ID")
    if st.button("送出"):
        delete_project(new_project_id)
        st.rerun()
def get_projects():
    return session.query(Project).all()

def add_project(name, description,create_user,create_time):
    new_project = Project(name=name, description=description,create_user=create_user,create_time=create_time)
    session.add(new_project)
    session.commit()

def edit_project(project_id, name, description):
    project = session.query(Project).filter_by(id=project_id).first()
    if project:
        project.name = name
        project.description = description
        session.commit()

def delete_project(project_id):
    project = session.query(Project).filter_by(id=project_id).first()
    if project:
        session.delete(project)
        session.commit()

# 創建一個 Streamlit 頁面
st.write("## :open_file_folder: 工程專案管理系統")

st.write("---")

session = get_session()

# 獲取所有專案
projects = get_projects()
projects_data = [{'ID': p.id, '工程名稱': p.name, '工程描述': p.description,"建立人員":p.create_user,"建立時間":p.create_time} for p in projects]
df = pd.DataFrame(projects_data)

# 顯示所有專案
st.write("### 專案清單")

df_projects = st.dataframe(df, use_container_width=True, hide_index=True)

project_act=st.selectbox("選擇動作",["新增專案","刪除專案"])

if st.button("執行"):

    if project_act=="新增專案":
        add_project_form()
    elif project_act=="刪除專案":
        delete_project_form()


# st.write("---")

# 創建選項列表，每個選項包含工程 ID 和名稱

project_options = [f"{row['ID']}: {row['工程名稱']}" for index, row in df.iterrows()]

selected_project = st.sidebar.selectbox("選擇目前使用專案", project_options)# 創建選項列表，每個選項包含工程 ID 和名稱
project_options = [f"{row['ID']}: {row['工程名稱']}" for index, row in df.iterrows()]

st.session_state['active_project_id'] = selected_project.split(':')[0]
st.session_state['active_project_name'] = selected_project.split(':')[1]

session.close()