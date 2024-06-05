# Router Management Automation with Selenium

This project provides a Python script to automate the login and reboot process for DG8045 routers and their family using Selenium WebDriver. The script handles the login to the router's web interface, navigates to the device management section, and initiates a reboot.

## Features

- Automates the login process to the router's web interface.
- Navigates to the device management section.
- Initiates a reboot of the router.
- Handles SSL certificate errors.
- Configurable for different routers in the DG8045 family.

## Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your version of Chrome)
- Please make sure the exe file of the driver is on the same folder of python file
## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/abdozeo/DG8045_automated_restart.git
    cd router-management-automation
    ```

2. **Install required Python packages**:

    ```sh
    pip install selenium
    ```

3. **Download ChromeDriver**:

    Download the ChromeDriver from the official site: [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in the project directory or specify its path in the script.

## Usage

1. **Configure your credentials**:

    Replace `ADD_YOUR_GATEWAY_PASSWORD_HERE` with your router's password in the script.

    ```python
    USR = "admin"
    PASS = "ADD_YOUR_GATEWAY_PASSWORD_HERE"
    ```

2. **Run the script**:

    Execute the script using Python:

    ```sh
    python main.py
    ```

## Script Overview

The script performs the following steps:

1. **Imports necessary modules**:

    ```python
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    ```

2. **Sets up Chrome options to ignore certificate errors**:

    ```python
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    ```

3. **Initializes the WebDriver**:

    ```python
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(options=options)
    ```

4. **Defines credentials**:

    ```python
    USR = "admin"
    PASS = "ADD_YOUR_GATEWAY_PASSWORD_HERE"
    ```

5. **Logs into the router's web interface**:

    ```python
    driver.get("http://192.168.1.1")
    username = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID,"index_username")))
    password = driver.find_element(By.ID,"password")
    username.send_keys(USR)
    password.send_keys(PASS + Keys.ENTER)
    time.sleep(3) # Successful Login
    ```

6. **Navigates to the device management section and initiates a reboot**:

    ```python
    driver.get("https://192.168.1.1/html/advance.html#device_mngt")
    time.sleep(5)
    btn = driver.find_element(By.ID,"rebootId")
    btn.click()
    time.sleep(5)
    sure_btn = driver.find_element(By.ID,"dev_mngt_modal_id_ok")
    sure_btn.click() # Reboot Successful
    time.sleep(5)
    driver.quit()
    ```


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.
