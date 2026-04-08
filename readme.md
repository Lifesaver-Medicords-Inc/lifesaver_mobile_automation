# Automation test for Lifesaver
Selenium + Appium POM framework iOS, and Android.

## Reference: [Test Plan](https://docs.google.com/document/d/19IyHtDgiK2Aycew_LxiKp4TJeYVwIyO_cj_uPQl8Wqo/edit?usp=sharing)


## Pre-requisites/Setup:
> Required Packages
> * Python
> * Selenium
> * Appium
> * Pytest
> * Allure

> install dependecies
> ```bash
> pip install -r requirements.txt
> ```

> For Android tests, also run Appium locally:
> ```bash
> npm install -g appium && appium
> ```
> Run Appium Server
> ```bash
> appium --address 0.0.0.0 --port 4723
> ```

> For Ios tests, also run Appium Server on Mac: 
> ```bash
> npm install -g appium && appium
> ```
> 
> Make sure to get udid
> ```bash
> idevice_id -l
> Sample output: 00008030-0019349E2660A02E
> ```
> 
> Get Ip
> ```bash
> ipconfig getifaddr en1
> ```
> 
> Run Appium Server
> ```bash
> appium --address 0.0.0.0 --port 4723
> ```


## Run Tests

| Command | What runs |
|---|---|
| `pytest -m smoke` | All smoke (iOS + Android) |
| `pytest -m "smoke and ios"` | iOS smoke only |
| `pytest -m "smoke and android"` | Android smoke only |
| `pytest -m regression` | Full regression suite |

### Extra flags
```bash
pytest -m "smoke and web" --env=staging --headless
pytest -m "smoke and web" --browser=firefox
pytest -m smoke --html=reports/report.html --self-contained-html
```

## Customising for Your App
2. **iOS** — update AccessibilityIDs in `pages/ios/` and set `.app` path in `drivers/mobile_driver_factory.py`
3. **Android** — update resource IDs in `pages/android/` and set `.apk` path in `drivers/mobile_driver_factory.py`
4. **Environments** — edit `config/dev|staging|prod.yaml` with your real URLs
