import streamlit as st
import pandas as pd

st.header(":clipboard: 契約項目")

st.markdown("---")

st.subheader(":one:契約檔案上傳")

# with st.expander("製作教學"):

#     st.markdown("[ExcelVBA @ PCCES後處理工具](https://hankvba.blogspot.com/2024/02/excel-vba-pcces.html)")

st.markdown("")

file=st.file_uploader("請上傳CSV檔案",type="csv")

st.markdown("---")

if  not file is None:

    st.subheader(":two: 詳細表調整")

    df=pd.read_csv(file)
    df_new = df.drop('Unnamed: 6', axis=1)
    st.data_editor(df_new,use_container_width=True,hide_index=True)

    btn=st.button("新增",type="primary")

    if btn:
        ## 上傳至資料庫
        df.to_csv("data.csv",index=False,encoding="utf-8-sig")
        st.toast("已經上傳成功!!!",icon="✅")

# st.markdown("---")

# st.subheader(":three: 選取資料")

# # 使用 .query() 方法筛选出單價不為0的項目
# df_filtered = df.query("單價 != 0")

# # 获取 '項目' 列的数据，并转换为列表
# items_list = df_filtered['項目'].tolist()

# # 显示 '項目' 列的 Selectbox
# selected_item = st.selectbox("選擇一個項目", items_list)

# st.write(selected_item)