import requests

def generate_otp(phone_number, country_code, headers):
    url_generate_otp = "https://www.district.in/gw/auth/generate_otp"
    payload_generate = {
        "phone_number": phone_number,
        "country_code": country_code
    }
    response_generate = requests.post(url_generate_otp, json=payload_generate, headers=headers)
    print("Generate OTP Status Code:", response_generate.status_code)
    try:
        response_data = response_generate.json()
        print("Generate OTP Response:", response_data)
        return response_data
    except requests.exceptions.JSONDecodeError:
        print("Generate OTP Response (Raw):", response_generate.text)
        return None

def verify_otp(phone_number, country_code, otp, headers):
    url_verify_otp = "https://www.district.in/gw/auth/validate_otp"
    payload_verify = {
        "phone_number": phone_number,
        "country_code": country_code,
        "otp": otp
    }
    response_verify = requests.post(url_verify_otp, json=payload_verify, headers=headers)
    print("Verify OTP Status Code:", response_verify.status_code)
    try:
        response_verify_data = response_verify.json()
        print("Verify OTP Response:", response_verify_data)
    except requests.exceptions.JSONDecodeError:
        print("Verify OTP Response (Raw):", response_verify.text)
