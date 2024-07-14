import streamlit as st
import mysql.connector
from datetime import datetime

# 设置数据库连接参数
DB_HOST = 'hkg1.clusters.zeabur.com'
DB_USER = 'root'
DB_PORT = '31222'
DB_PASSWORD = 'j8Y274rZGq05zK3IvoOQJR9fxsUH61uL'
DB_DATABASE = 'daily_report'

# @st.cache_resource
def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE
    )

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INT AUTO_INCREMENT PRIMARY KEY,
            contract_number VARCHAR(100),
            project_name VARCHAR(100),
            user_name VARCHAR(100),
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

def add_project(contract_number, project_name, user_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO projects (contract_number, project_name, user_name) VALUES (%s, %s, %s)', 
                   (contract_number, project_name, user_name))
    conn.commit()
    cursor.close()
    conn.close()

def get_projects():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM projects')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def update_project(project_id, contract_number, project_name, user_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE projects SET contract_number=%s, project_name=%s, user_name=%s WHERE id=%s', 
                   (contract_number, project_name, user_name, project_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_project(project_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM projects WHERE id=%s', (project_id,))
    conn.commit()
    cursor.close()
    conn.close()

st.title('Streamlit MySQL CRUD - 工程專案')

create_table()

# Create
st.header('新增工程專案')
contract_number = st.text_input('契約編號')
project_name = st.text_input('工程名稱')
user_name = st.text_input('建立人員')
if st.button('新增專案'):
    add_project(contract_number, project_name, user_name)
    st.success('工程專案新增成功')

# Read
st.header('查看工程專案')
projects = get_projects()
for project in projects:
    st.write(f"ID: {project[0]}, 契約編號: {project[1]}, 工程名稱: {project[2]}, 建立人員: {project[3]}, 建立日期: {project[4]}")

# Update
st.header('編輯工程專案')
project_id = st.number_input('專案ID', min_value=1, step=1)
new_contract_number = st.text_input('新契約編號')
new_project_name = st.text_input('新工程名稱')
new_user_name = st.text_input('新建立人員')
if st.button('更新專案'):
    update_project(project_id, new_contract_number, new_project_name, new_user_name)
    st.success('工程專案更新成功')

# Delete
st.header('刪除工程專案')
del_project_id = st.number_input('要刪除的專案ID', min_value=1, step=1)
if st.button('刪除專案'):
    delete_project(del_project_id)
    st.success('工程專案刪除成功')
