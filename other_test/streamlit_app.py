# import streamlit as st

# ## session_state init

# if 'user_id' not in st.session_state:
#     st.session_state.user_id=""

# ## navigation

# st.logo("logo.jpg")

# p1=st.Page("views/page_login.py",title="登入",icon=":material/home:")
# p2=st.Page("views/page_jobs.py",title="工程專案",icon=":material/add:")
# p3=st.Page("views/page3.py",title="基本資料",icon=":material/open_in_new:")


# pg=st.navigation({
#     "主要功能":[p1],
#     "專案":[p2,p3]
# })

# pg.run()

# ## formula


import streamlit as st


ROLES = [None, "Requester", "Responder", "Admin"]


role = st.session_state.role


request_1 = st.Page(
    "views/page_jobs.py",
    title="Request 1",
    icon=":material/help:",
    default=(role == "Requester"),
)
request_2 = st.Page(
    "views/page_login.py", title="Request 2", icon=":material/bug_report:"
)
respond_1 = st.Page(
    "views/page3.py",
    title="Respond 1",
    icon=":material/healing:",
    default=(role == "Responder"),
)


request_pages = [request_1, request_2]
respond_pages = [respond_1]


st.title("Request manager")


pg = st.navigation({"bb2":request_pages,"nn2":respond_pages})


pg.run()