import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def plot_progress_chart(df):
    
    # 確保日期欄位是 datetime 格式
    df['date'] = pd.to_datetime(df['date'])
    
    # 繪製圖表
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['sum_progress(%)'], marker='o')
    # plt.xlabel('Date')
    plt.ylabel('Progress (%)')
    # plt.title('累積進度 (%) 隨日期變化圖')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # 顯示圖表
    st.pyplot(plt)

st.header("	:date: 進度項目")

st.markdown("---")

st.subheader(":one:進度檔案上傳")

st.markdown("")

file=st.file_uploader("請上傳CSV檔案",type="csv")

st.markdown("---")

if  not file is None:

    st.subheader(":two: 進度表調整")

    df=pd.read_csv(file)

    df_editor=st.data_editor(df,hide_index=True)

    # plot_progress_chart(df_editor)

    btn=st.button("新增",type="primary")

    if btn:
        ## 上傳至資料庫
        df.to_csv("pgs.csv",index=False,encoding="utf-8-sig")
        st.toast("已經上傳成功!!!",icon="✅")