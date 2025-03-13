import requests

# Headers for fetching billing details
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
    "x-device-id": "79224e42-dd7d-4ad8-9387-4cfec752e7a6",
    "x-access-token": "1741838694574633741_2615493909387007317_a9da4c68c5a3f754a9b8a35fe0b69b8818ad1fe54ad34e72a8e4442bd5365995",
    "x-refresh-token": "1741838694574639446_6206202887448197281_2a0d75b61d2342abb158ab6baa0092f8e5602fec45a9fa907cea46ead3a948e1",
    "cookie": "YOUR_COOKIES_HERE"  # Replace with actual cookies if required
}

def get_billing_details():
    url_billing_details = "https://www.district.in/gw/consumer/events/v1/user/userProfile"

    try:
        response = requests.get(url_billing_details, headers=billing_headers)
        print("Billing Details Status Code:", response.status_code)

        if response.status_code == 200:
            response_data = response.json()
            print("Billing Details Response:", response_data)
            return response_data
        else:
            print(f"Error: Received status code {response.status_code}")
            print("Response Text:", response.text)
            return None
    except requests.RequestException as e:
        print("Request failed:", str(e))
        return None

if __name__ == "__main__":
    print("Fetching billing details...")
    billing_details = get_billing_details()
    if billing_details:
        print("Billing Details:", billing_details)
    else:
        print("Failed to retrieve billing details.")
