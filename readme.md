# Lifesaver Mobile Automation
Appium + Pytest POM framework for iOS and Android.

## Reference: [Test Plan](https://docs.google.com/document/d/19IyHtDgiK2Aycew_LxiKp4TJeYVwIyO_cj_uPQl8Wqo/edit?usp=sharing)

---

## Project Structure
```
Lifesaver_mobile_automation/
├── config/
│   ├── android_caps.py       ← Android device capabilities
│   └── ios_caps.py           ← iOS device capabilities
├── pages/
│   ├── base_page.py          ← shared actions (tap, type, scroll)
│   ├── android/              ← Android page objects
│   └── ios/                  ← iOS page objects
├── tests/
│   ├── android/
│   │   ├── smoke/
│   │   └── regression/
│   └── ios/
│       ├── smoke/
│       └── regression/
├── utils/
│   └── logger_utils.py       ← logging + screenshot on failure
├── conftest.py               ← fixtures, driver setup
├── pytest.ini
└── requirements.txt
```

---

## Pre-requisites

- Python 3.10+
- Node.js 18+
- Appium 2.x
- Android: ADB + connected device or emulator
- iOS: Xcode + connected iPhone (Mac only)

### Install Python dependencies
```bash
pip install -r requirements.txt
```

### Install Appium
```bash
npm install -g appium
```

### Install Appium drivers
```bash
# Android
appium driver install uiautomator2

# iOS
appium driver install xcuitest
```

---

## Device Setup

### Android
```bash
# 1. Connect device via USB or start emulator

# 2. Verify device is detected
adb devices
# output:
# List of devices attached
# 8T4PHMPZRO8L7LVS    device   ← copy this UDID

# 3. Paste UDID into config/android_caps.py
android_caps = {
    "appium:udid": "8T4PHMPZRO8L7LVS",   # ← paste here
    ...
}
```

### iOS (Mac only)
```bash
# 1. Connect iPhone via USB

# 2. Get UDID
idevice_id -l
# output: 00008030-0019349E2660A02E   ← copy this

# 3. Get Mac IP (for remote Appium server)
ipconfig getifaddr en1

# 4. Paste UDID into config/ios_caps.py
ios_caps = {
    "appium:udid": "00008030-0019349E2660A02E",   # ← paste here
    ...
}
```

---

## Running Appium Server

### Android (Windows or Mac)
```bash
appium --address 127.0.0.1 --port 4723
```

### iOS (Mac only)
```bash
appium --address 0.0.0.0 --port 4723
```

> Keep Appium running in a separate terminal before running tests.

---

## Run Tests

### Android
```bash
# all android tests
pytest tests/android/ --platform android

# smoke only
pytest tests/android/smoke/ --platform android

# regression only
pytest tests/android/regression/ --platform android
```

### iOS
```bash
# all ios tests
pytest tests/ios/ --platform ios

# smoke only
pytest tests/ios/smoke/ --platform ios

# regression only
pytest tests/ios/regression/ --platform ios
```

### With extra flags
```bash
# verbose output + show logs in terminal
pytest tests/android/ --platform android -v -s

# stop after first failure
pytest tests/android/ --platform android -x

# run specific test file
pytest tests/android/smoke/test_login.py --platform android

# run specific test
pytest tests/android/smoke/test_login.py::TestAndroidLoginSmoke::test_email_login_success --platform android
```

---

## Allure Reports

```bash
# run tests (results saved to allure-results/ automatically)
pytest tests/android/ --platform android

# open report in browser
allure serve allure-results

# install allure CLI (if not installed)
# mac
brew install allure
# windows
scoop install allure
```

---

## Configuration Files

| File | What to update |
|---|---|
| `config/android_caps.py` | UDID, device name, app package, server URL |
| `config/ios_caps.py` | UDID, bundle ID, Xcode org ID, server URL |
| `conftest.py` | Test credentials in `logged_in_driver` fixture |
