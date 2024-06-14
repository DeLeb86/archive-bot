import requests
import streamlit as st
st.title("Archie")

apiKey="fbPOjL0yn8BKWhpQVS5f9iCfPSrLgReK"
#apiKey=st.secrets["key"]
headers={
    "Content-Type" : "application/json",
    "Authorization": "Bearer " + apiKey
    }
form = st.form(key='my-form')
question = form.text_input('Votre question ici.. ')
submit_button = form.form_submit_button(label='Submit')
if submit_button: 
    
    r=requests.post("https://masterclass-right-project-zoojr.westeurope.inference.ml.azure.com/score",json={"Input":question},headers=headers)
    st.markdown(r.json()["Response"])    
