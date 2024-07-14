import streamlit as st
import mysql.connector
from mysql.connector import errorcode

# 設定資料庫連接參數
DB_HOST = 'hkg1.clusters.zeabur.com'
DB_USER = 'root'
DB_PORT='31222'
DB_PASSWORD = 'j8Y274rZGq05zK3IvoOQJR9fxsUH61uL'
DB_DATABASE = 'daily_report'

# 建立資料庫連接並創建資料庫（如果不存在）
# @st.cache_resource
# 創建資料庫連接
def create_connection(host, port, user, password, database):
    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    return connection

# 執行查詢
def execute_query(connection, query, params=None):
    cursor = connection.cursor()
    cursor.execute(query, params or ())
    connection.commit()
    cursor.close()

# 獲取查詢結果
def fetch_query(connection, query, params=None):
    cursor = connection.cursor()
    cursor.execute(query, params or ())
    records = cursor.fetchall()
    cursor.close()
    return records

# Streamlit 應用的主邏輯
st.title("工程專案管理系統")

# 新增工程專案
with st.form(key='project_form'):
    contract_number = st.text_input("契約編號")
    project_name = st.text_input("工程名稱")
    creator = st.text_input("建立人員")

    if st.form_submit_button("新增專案"):

        print(contract_number,project_name,creator)
        if contract_number and project_name and creator:
            conn = create_connection(DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_DATABASE)
            query = "INSERT INTO projects (contract_number, project_name, creator) VALUES (%s, %s, %s)"
            params = (contract_number, project_name, creator)

            try:
                execute_query(conn, query, params)
                st.success("工程專案新增成功！")
            except mysql.connector.Error as err:
                st.error(f"Failed to insert into database: {err}")
            finally:
                conn.close()
        else:
            st.error("所有欄位都是必填的")
            

# # 顯示已經存在的專案列表
# st.subheader("現有工程專案")
# conn = create_connection(DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_DATABASE)
# query = "SELECT contract_number, project_name, creator, created_date FROM projects"
# try:
#     rows = fetch_query(conn, query)
#     if rows:
#         for row in rows:
#             st.write(f"契約編號: {row[0]}, 工程名稱: {row[1]}, 建立人員: {row[2]}, 建立日期: {row[3]}")
#     else:
#         st.write("目前沒有工程專案")
# except mysql.connector.Error as err:
#     st.error(f"Failed to fetch data from database: {err}")
# finally:
#     conn.close()