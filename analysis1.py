import pandas as pd
import streamlit as st
import plotly.express as px
import base64
from io import StringIO, BytesIO

st.set_page_config(page_title="anlasysis1")
st.header("tips analysis")
st.subheader("analysis practis")
st.write("zabbby el 7nen")
uploaded_file = st.file_uploader("please upload your file", type = "xlsx")
if uploaded_file:
    st.markdown("---")
    df = pd.read_excel(uploaded_file, engine = 'openpyxl')
    


# df = pd.read_csv("C:/Users/Dell/Desktop/WH_analysis/tips.csv")
# st.table(df)
# st.dataframe(df)

tab1, tab2 = st.tabs(["summary", "details"])

with tab2:
    col11, col12, col13, col14 = st.columns(4, gap = "large")
    with col11:
        day_sel = st.selectbox( "choose day",sorted((df['day'].unique())))
        mask1 = df["day"] == day_sel
        
    with col12:
         sex_sel = st.multiselect("select gender", df["sex"].unique())
         mask2 = (df["sex"].isin(sex_sel))
         
         
         
    with col13:
         smoker_sel = st.radio("smokingcondition", df["smoker"].unique())
         mask3 = df["smoker"] == smoker_sel
         
         
    with col14:
        size_sel = st.slider("selectsize", df["size"].min(), df["size"].max(), value = (df["size"].min(), df["size"].max()))
        mask4 = df["size"].between(*size_sel)
        
        mask = mask1 & mask2 & mask3 & mask4
        val = round((((df[mask]["total_bill"].sum())/(df["total_bill"].sum()))*100),2)
        st.metric(label = "totalsales", value = df[mask]["total_bill"].sum(), delta = f'{val} %')
    
    col21, col22, col23, col24 = st.columns(4, gap = "large")
    with col21:
        maskn = mask2 & mask3 & mask4
        bar1_chart = px.bar(df[mask2], x = df[mask2]["day"], y = df[mask2]["total_bill"], title = "total bills", text_auto =False, orientation = "v", barmode = "overlay", template = "plotly", width = 500)
        st.plotly_chart(bar1_chart)
    
    col31, col32, col33, col34 = st.columns(4, gap = "large")
    
    
    col41, col42, col43, col44 = st.columns(4, gap = "large")