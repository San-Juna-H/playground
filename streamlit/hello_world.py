import streamlit as st

# 제목 설정
st.title("안녕하세요, Streamlit!")

# 텍스트 입력
user_input = st.text_input("당신의 이름을 입력하세요:")

# 버튼 클릭 시 반응
if st.button("제출"):
    st.write(f"안녕하세요, {user_input}님!")
