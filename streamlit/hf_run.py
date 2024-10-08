import streamlit as st
import requests

# HuggingFace API call function
def run_model(model_id, access_token, prompt):
    API_URL = f"https://api-inference.huggingface.co/models/{model_id}"
    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {
        "inputs": prompt,
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Title
st.title("HuggingFace Serverless API Inference")

# hyperlink for further information
st.markdown("### [Available HuggingFace Models](https://huggingface.co/models?inference=warm&pipeline_tag=text-generation&sort=trending)")  
st.markdown("[For more details, please refer to the HuggingFace API documentation](https://huggingface.co/docs/api-inference/parameters)")  

# model_id, access_token input
model_id = st.text_input("Model ID")
access_token = st.text_input("Access Token", type="password")

# model input
model_input = st.text_input("Input")

# Generate
if st.button("Generate"):
    model_output = run_model(model_id, access_token, model_input)
    st.write("Output:")
    st.write(model_output)

# install streamlit : conda install -c conda-forge streamlit
# install requests : conda install -c conda-forge requests
# run this command in terminal : streamlit run hf_run.py