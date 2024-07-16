import streamlit as st

## session_state init

# if 'user_id' not in st.session_state:
#     st.session_state.user_id=""

## navigation

# st.logo("logo.jpg")

p1=st.Page("views/information.py",title="基本資料",icon=":material/home:")
p2=st.Page("views/contract.py",title="契約項目",icon=":material/add:")
p3=st.Page("views/progress.py",title="進度設定",icon=":material/open_in_new:")
p4=st.Page("views/projects.py",title="工程專案",icon=":material/open_in_new:")

pg=st.navigation([p4,p1,p2,p3])

# pg=st.navigation({
#     "主要功能":[p1,p4],
#     "專案":[p2,p3]
# })

pg.run()