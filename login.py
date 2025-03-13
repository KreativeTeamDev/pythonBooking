import requests

url_generate_otp = "https://www.district.in/gw/auth/generate_otp"
url_verify_otp = "https://www.district.in/gw/auth/validate_otp"


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.district.in",
    "referer": "https://www.district.in/",
    "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "x-app-type": "ed_web",
    "x-device-id": "d383caea-c92d-481a-afd0-b95d4a2e2cad",
    "cookie": "YOUR_COOKIES_HERE"  # Replace this with actual cookies if required
}

# Generate OTP
payload_generate = {
    "phone_number": "8101844250",
    "country_code": "91"
}

response_generate = requests.post(url_generate_otp, json=payload_generate, headers=headers)
print("Generate OTP Status Code:", response_generate.status_code)
try:
    response_data = response_generate.json()
    print("Generate OTP Response:", response_data)
except requests.exceptions.JSONDecodeError:
    print("Generate OTP Response (Raw):", response_generate.text)
    response_data = None

if response_data:
    otp = input("Enter the OTP received: ")
    
    # Verify OTP
    payload_verify = {
        "phone_number": "8101844250",
        "country_code": "91",
        "otp": otp
    }
    
    response_verify = requests.post(url_verify_otp, json=payload_verify, headers=headers)
    print("Verify OTP Status Code:", response_verify.status_code)
    try:
        response_verify_data = response_verify.json()
        print("Verify OTP Response:", response_verify_data)
    except requests.exceptions.JSONDecodeError:
        print("Verify OTP Response (Raw):", response_verify.text)
