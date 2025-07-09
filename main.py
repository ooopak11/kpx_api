from api import get_analog, send_control

device_id = "DEVICE_ID_1"

print("\n[1] analog 데이터 요청")
analog_data = get_analog(device_id)
if analog_data:
    print("analog 수신:", analog_data)

print("\n[2] 제어 지령 전송")
control_response = send_control(device_id, targetPower=1500000)
if control_response:
    print("제어 응답:", control_response)


