import streamlit as st

def run_model(model_info, model_input):
    # 모델 실행 로직 구현
    model_output = model_info + model_input
    return model_output

# 제목 설정
st.title("HuggingFace model Run")

# 모델 정보 입력
model_info = st.text_input("model id")

# 모델 input
model_input = st.text_input("Input")

# 모델 실행 
model_output = run_model(model_info, model_input)

# 모델 실행 결과 출력
st.write(f"Output: {model_output}")

# install streamlit : conda install -c conda-forge streamlit
# run this command in terminal : streamlit run hf_run.py