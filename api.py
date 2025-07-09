import requests
from datetime import datetime

BASE_URL = "http://210.98.1.10:5002/api"  # 실제 EMS 서버 주소로 교체


def get_analog(did: str, isVpp=True, isSCDG=False):
    url = f"{BASE_URL}/kpx/ems/analog"
    params = {
        "did": did,
        "isVpp": str(isVpp),
        "isSCDG": str(isSCDG)
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"[ERROR] analog 요청 실패: {e}")
        return None


def send_control(did: str, targetPower: int, isVpp=True, isSCDG=False):
    url = f"{BASE_URL}/kpx/ems/control"
    payload = {
        "did": did,
        "controlMode": "limit",
        "targetPower": targetPower,
        "requestAt": int(datetime.now().strftime("%Y%m%d%H%M%S")),
        "isVpp": isVpp,
        "isSCDG": isSCDG
    }

    try:
        response = requests.post(url, json=payload, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"[ERROR] control 요청 실패: {e}")
        return None
