import requests
from otp_service import generate_otp, verify_otp
from aboutUser import get_billing_details

def main():
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
        "x-device-id": "7e63bbe9-86f3-4813-9516-73c773f580d4",
        "cookie": "YOUR_COOKIES_HERE"  # Replace this with actual cookies if required
    }
    

    billing_headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "origin": "https://www.district.in",
    "referer": "https://www.district.in/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "x-app-type": "ed_web",
    "x-device-id": "7e63bbe9-86f3-4813-9516-73c773f580d4",
    "authorization": "Bearer YOUR_ACCESS_TOKEN_HERE",  # If required
    "cookie": "YOUR_COOKIES_HERE"  # Replace with actual cookies if needed
}
    phone_number = "8101844250"
    country_code = "91"
    
    response_data = generate_otp(phone_number, country_code, headers)
    
    if response_data:
        otp = input("Enter the OTP received: ")
        verify_response = verify_otp(phone_number, country_code, otp, headers)
        
        if verify_response:
            print("Fetching billing details...")
            billing_details = get_billing_details(billing_headers)
            print("Billing Details:", billing_details)

if __name__ == "__main__":
    main()
