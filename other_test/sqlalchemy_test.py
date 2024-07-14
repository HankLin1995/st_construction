# from sqlalchemy import create_engine, Column, Integer, String,text
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# # 創建數據庫引擎和會話
# engine = create_engine('mysql+mysqlconnector://root:a0912052274@localhost:3306/engineering_qc')
# Session = sessionmaker(bind=engine)
# session = Session()

# # 創建基本模型
# Base = sqlalchemy.orm.declarative_base()

# # 定義數據庫表的模型
# class NewTable(Base):
#     __tablename__ = 'new_table'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     age = Column(Integer)

# # 創建表格
# Base.metadata.create_all(engine)

# # CRUD 操作示例

# # 創建數據
# def create_data(name, age):
#     new_data = NewTable(name=name, age=age)
#     session.add(new_data)
#     session.commit()

# # 查詢數據
# def query_data():
#     return session.query(NewTable).all()

# # 更新數據
# def update_data(id, name, age):
#     data = session.query(NewTable).filter_by(id=id).first()
#     if data:
#         data.name = name
#         data.age = age
#         session.commit()

# # 刪除數據
# def delete_data(id):
#     data = session.query(NewTable).filter_by(id=id).first()
#     if data:
#         session.delete(data)
#         session.commit()

# # 使用示例
# if __name__ == "__main__":
#     # 創建數據
#     create_data('Alice', 30)

#     # 查詢數據
#     results = query_data()
#     for result in results:
#         print(f"ID: {result.id}, Name: {result.name}, Age: {result.age}")

#     # 更新數據
#     update_data(1, 'Bob', 25)

#     # 刪除數據
#     # delete_data(1)

#     # 查詢更新後的數據
#     updated_results = query_data()
#     # for result in updated_results:
#     #     print(f"ID: {result.id}, Name: {result.name}, Age: {result.age}")

#     # 關閉會話

#     engine = create_engine('mysql+mysqlconnector://root:a0912052274@localhost:3306/engineering_qc')

#     session.close()

#=====================================

# from sqlalchemy import create_engine, text
# from sqlalchemy.orm import sessionmaker

# # 創建資料庫引擎
# engine = create_engine('mysql+mysqlconnector://root:a0912052274@localhost:3306/engineering_qc')

# # 創建一個會話
# Session = sessionmaker(bind=engine)
# session = Session()

# # 定義 ALTER TABLE 語句
# alter_sql = text('ALTER TABLE projects ADD COLUMN new_column_name VARCHAR(255)')

# # 執行 ALTER TABLE 語句
# session.execute(alter_sql)
# session.commit()

# # 關閉會話
# session.close()

import streamlit as st
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship,declarative_base

# 建立資料庫連線
engine = create_engine('mysql+mysqlconnector://root:a0912052274@localhost:3306/engineering_qc',echo=False)#, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# 資料庫模型定義
class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    contracts = relationship("Contract", back_populates="project")

class Contract(Base):
    __tablename__ = 'contracts'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    project_id = Column(Integer, ForeignKey('projects.id'))
    project = relationship("Project", back_populates="contracts")

# 創建資料庫表格
Base.metadata.create_all(engine)

# Streamlit App
st.title('工程管理系統')

# 創建工程專案
st.subheader('新增工程專案')
project_name = st.text_input('輸入工程名稱')
if st.button('新增工程'):
    if project_name:
        existing_project = session.query(Project).filter_by(name=project_name).first()
        if existing_project:
            st.warning(f'工程名稱 "{project_name}" 已存在。')
        else:
            new_project = Project(name=project_name)
            session.add(new_project)
            session.commit()
            st.success(f'成功新增工程名稱 "{project_name}"。')
    else:
        st.warning('請輸入工程名稱。')

# 新增契約文件
st.subheader('新增契約文件')
project_names = [project.name for project in session.query(Project).all()]
selected_project = st.selectbox('選擇工程專案', project_names)
contract_name = st.text_input('輸入契約文件名稱')
if st.button('新增契約文件'):
    if contract_name:
        project = session.query(Project).filter_by(name=selected_project).first()
        if project:
            existing_contract = session.query(Contract).filter_by(name=contract_name, project_id=project.id).first()
            if existing_contract:
                st.warning(f'在工程 "{selected_project}" 下已存在名稱為 "{contract_name}" 的契約文件。')
            else:
                new_contract = Contract(name=contract_name, project_id=project.id)
                session.add(new_contract)
                session.commit()
                st.success(f'成功新增契約文件 "{contract_name}" 到工程 "{selected_project}"。')
        else:
            st.warning(f'未找到名為 "{selected_project}" 的工程專案。')
    else:
        st.warning('請輸入契約文件名稱。')
# 刪除工程專案或契約文件
st.subheader('刪除工程專案或契約文件')

# 刪除工程專案
project_to_delete = st.selectbox('選擇要刪除的工程專案', project_names)
if st.button('刪除工程專案'):
    project = session.query(Project).filter_by(name=project_to_delete).first()
    if project:
        session.delete(project)
        session.commit()
        st.success(f'成功刪除工程專案 "{project_to_delete}"。')
    else:
        st.warning(f'未找到名為 "{project_to_delete}" 的工程專案。')

# 刪除契約文件
contract_names = [contract.name for contract in session.query(Contract).all()]
contract_to_delete = st.selectbox('選擇要刪除的契約文件', contract_names)
if st.button('刪除契約文件'):
    contract = session.query(Contract).filter_by(name=contract_to_delete).first()
    if contract:
        session.delete(contract)
        session.commit()
        st.success(f'成功刪除契約文件 "{contract_to_delete}"。')
    else:
        st.warning(f'未找到名為 "{contract_to_delete}" 的契約文件。')

# 更新契約文件
st.subheader('更新契約文件')
contract_names = [contract.name for contract in session.query(Contract).all()]
contract_to_update = st.selectbox('選擇要更新的契約文件', contract_names)
new_contract_name = st.text_input('輸入新的契約文件名稱')
if st.button('更新契約文件'):
    if new_contract_name:
        contract = session.query(Contract).filter_by(name=contract_to_update).first()
        if contract:
            contract.name = new_contract_name
            session.commit()
            st.success(f'成功更新契約文件名稱 "{contract_to_update}" 為 "{new_contract_name}"。')
        else:
            st.warning(f'未找到名為 "{contract_to_update}" 的契約文件。')
    else:
        st.warning('請輸入新的契約文件名稱。')

# 關閉資料庫連接
session.close()
