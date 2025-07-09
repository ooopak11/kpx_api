import streamlit as st
from api import get_analog, send_control

st.title("KPX → EMS 연동 대시보드")

did = st.text_input("장치 ID", "DEVICE_ID_1")

if st.button("analog 요청"):
    data = get_analog(did)
    if data:
        st.success("수신 완료")
        st.json(data)

target_power = st.number_input(
    "출력 목표값 (W)", min_value=0, step=1000, value=1000000)

if st.button("제어 지령 전송"):
    result = send_control(did, target_power)
    if result:
        st.success("제어 응답 수신")
        st.json(result)
