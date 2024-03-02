import streamlit as st
import requests
st.title("My hello world initial app")

st.write ("First step for mvp")

value1= st.slider('select an emotion value', min_value =0, max_value=4,value=1,step=1)
#will be used for predict
#example: response=requests.get(f"https://mvp-wjxeo2hbwa-ew.a.run.app/predict?emotion={value1}").json()
response=requests.get(f"https://mvp-wjxeo2hbwa-ew.a.run.app/").json()

st.write("The output is ", str(response))
