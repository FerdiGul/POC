
# 🧪 Vulnerable IoT Washer - Account Takeover PoC

This repository provides a Proof of Concept (PoC) for an **Account Takeover (ATO)** vulnerability discovered in a mobile application used to control IoT smart appliances (e.g., smart washers). The vulnerability was identified during a black-box penetration test targeting the iOS version of the application.

<img width="1227" alt="Vulnerable IoT Washer_ Pentest Flow Diagram" src="https://github.com/user-attachments/assets/f79b9ca6-942a-4e0a-91ed-eb64b9ab7a9d" />

![PoC_Response](https://github.com/user-attachments/assets/16928315-6bda-4308-a173-b8a23771d318)

---

## 🔍 Vulnerability Summary


- **Type**: Account Takeover (ATO)
- **CWE**: [CWE-287](https://cwe.mitre.org/data/definitions/287.html) – Improper Authentication
- **Estimated CVSS from HIGH to CRITICAL
- **Test Date**: 2025-05-10
- **Environment**: iOS Device + Burp Suite + Wireshark
- **Target Device**: IoT Smart Appliance (e.g., Washer)
- **Network Context**: Internal Wi-Fi, Proxy Server

---

## 📌 Summary

The mobile app failed to invalidate session refresh tokens after logout or device reboot. This allowed:

- Unlimited reuse of refresh tokens
- Persistent validity even after logout
- Generation of new access tokens (accessKey, secretKey, sessionToken)
- Full control over the user's connected IoT devices and home data

---

## ⚙️ Technical Background

### ✅ Expected Secure Behavior

- Refresh tokens should expire shortly after logout
- Tokens should be single-use only
- App should enforce device-specific binding (e.g., IP, DeviceID)
- Rate limits should be in place for sensitive operations

### ❌ Observed Weak Behavior

- `refreshToken` remains valid post-logout and post-reboot
- Tokens are reusable an unlimited number of times
- Full API access is possible without any re-authentication

---

## 📦 PoC: Refresh Token Reuse

This repository includes a demonstration script that:

1. Captures a valid refresh token from an authorized session
2. Reuses the token to generate new access tokens
3. Executes authenticated API calls without user interaction

> **Note**: For ethical reasons, no sensitive information or production tokens are included in this repository.

---

## 🎯 Impact Analysis

| Category            | Impact Description                                                                 |
|---------------------|-------------------------------------------------------------------------------------|
| Account Takeover    | Full user access for any attacker capturing a valid refresh token                  |
| Device Hijack       | IoT appliance control (e.g., start, stop, modify appliance behavior)               |
| Persistence         | Tokens valid across app logouts and device reboots                                 |
| Scope               | All users of the app may be impacted                                               |
| Attack Feasibility  | Easy in a shared Wi-Fi or proxy-enabled environment (MITM)                         |

---

## 🔁 Logout Test Results

| Action                     | Result                          |
|----------------------------|----------------------------------|
| User logs out              | `refreshToken` remains valid ❌ |
| Device reboot              | Token validity persists     ❌ |
| Generate new access token  | Success ✅                     |
| API access with new token  | Authorized ✅                  |

---

## 🛡️ Security Classification

| CWE ID   | Description                                                        |
|----------|--------------------------------------------------------------------|
| CWE-287  | Improper Authentication                                            |
| CWE-306  | Missing Authentication for Critical Function                       |
| CWE-384  | Session Fixation (Token binding not enforced or revoked properly)  |

---

## 🧩 Recommended Remediations

- Invalidate refresh tokens after logout
- Enforce device-based token binding (DeviceID, IP, etc.)
- Implement single-use refresh tokens
- Apply strict token expiration and rate limiting
- Use secure token revocation mechanisms

---

## 📍 Conclusion

This vulnerability enables persistent unauthorized access to smart appliances via insecure session handling. Even a low-privileged internal attacker (e.g., someone on the same Wi-Fi) can exploit this flaw to take over accounts and control IoT devices.

> 🛑 **Severity: Critical** – Immediate remediation is strongly recommended.

---

## 📁 Files

- `VulnWasher.py`: Demonstrates token reuse and API access

---

## ⚠️ Disclaimer

This repository is for **educational and research purposes only**. The author does not condone unauthorized access to any systems. All testing was performed in a controlled environment with explicit permission.


