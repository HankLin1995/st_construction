import streamlit as st
# import mysql.connector
import requests
import json

# # MySQL database configuration
# db_config = {
#     'user': 'your_mysql_username',
#     'password': 'your_mysql_password',
#     'host': 'your_mysql_host',
#     'database': 'mydatabase'
# }

# LINE OAuth 2 client setup
line_client_id = "2002566613"
line_client_secret = "db5f84506fb5e396ff22c9746eeb6277"
redirect_uri = "http://localhost:8501"
line_authorization_base_url = "https://access.line.me/oauth2/v2.1/authorize"
line_token_url = "https://api.line.me/oauth2/v2.1/token"
line_userinfo_url = "https://api.line.me/v2/profile"

# def save_user(provider, provider_user_id, email, name):
#     connection = mysql.connector.connect(**db_config)
#     cursor = connection.cursor()
#     cursor.execute("INSERT INTO users (provider, provider_user_id, email, name) VALUES (%s, %s, %s, %s)",
#                    (provider, provider_user_id, email, name))
#     connection.commit()
#     cursor.close()
#     connection.close()
st.title("LINE Login Example")
button_html = """
    <style>
    .line-login {
        background-color: #00c300;
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .line-login:hover {
        background-color: #00a300;
    }
    </style>
    <button class="line-login" onclick="startProcessing()">LINE 登入</button>
    <script>
    function startProcessing() {
        var input = document.getElementById('image-url-input').value;
        var inputEvent = new Event('input', { bubbles: true });
        var textArea = document.querySelector('textarea');
        textArea.value = input;
        textArea.dispatchEvent(inputEvent);
    }
    </script>
"""

# 在 Streamlit 中插入自定義按鈕
st.markdown(button_html, unsafe_allow_html=True)

request_uri = (
        f"{line_authorization_base_url}?response_type=code&client_id={line_client_id}"
        f"&redirect_uri=http://localhost:8501&state=random_string&scope=profile%20openid%20email"
    )
st.link_button('Login with LINE',url=request_uri)

# if st.button('Login with LINE'):
#     request_uri = (
#         f"{line_authorization_base_url}?response_type=code&client_id={line_client_id}"
#         f"&redirect_uri=http://localhost:8501&state=random_string&scope=profile%20openid%20email"
#     )
#     st.write(f"Click [here]({request_uri}) to login with LINE")

# Process LINE callback

if 'code' in st.query_params and 'state' in st.query_params:

    code = st.query_params['code']
    state = st.query_params['state']

    url = "https://api.line.me/oauth2/v2.1/token"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # 請求的數據
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': line_client_id,
        'client_secret': line_client_secret
    }

    # 發送 POST 請求
    response = requests.post(url, headers=headers, data=data)

    token_json=response.json()

    # 打印響應結果
    st.write("Status Code:", response.status_code)

    if response.status_code==200:

        # st.write("Response JSON:", response.json())

        access_token = token_json['access_token']
        userinfo_response = requests.get(
            line_userinfo_url,
            headers={'Authorization': f'Bearer {access_token}'}
        )
        userinfo_json = userinfo_response.json()
        # st.write(userinfo_json)
        user_id = userinfo_json['userId']
        display_name = userinfo_json['displayName']
        # save_user("line", user_id, None, display_name)
        st.write(f"Logged in as {display_name}")
        st.image( userinfo_json['pictureUrl'],width=50)