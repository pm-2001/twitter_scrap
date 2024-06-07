from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# webscrapping for proxies
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome()
driver.get("https://sslproxies.org/")
driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//table[@class='table table-striped table-bordered']//th[contains(., 'IP Address')]"))))
ips = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered']//tbody//tr//td[position() = 1]")))]
ports = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered']//tbody//tr//td[position() = 2]")))]
driver.quit()

# list of proxies
proxies = []
for i in range(0, len(ips)):
    proxies.append(ips[i]+':'+ports[i])

# webscrapping twitter using different proxies
for i in range(0, len(proxies)):
    try:
        print("Proxy selected: {}".format(proxies[i]))
        options = webdriver.ChromeOptions()
        options.add_argument('--proxy-server={}'.format(proxies[i]))
        driver = webdriver.Chrome(options=options)
        driver.get('https://x.com/i/flow/login')
        # driver.maximize_window()
        driver.implicitly_wait(10)

        username_field = driver.find_element(By.XPATH, "//input[@autocomplete='username']")
        username_field.send_keys('')
        next_button = driver.find_element(By.XPATH, "//button[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-ywje51 r-184id4b r-13qz1uu r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']")
        next_button.click()
        print("1")
        driver.implicitly_wait(10) 

        password_field = driver.find_element(By.XPATH, "//input[@autocomplete='current-password']")
        password_field.send_keys('')
        login_button = driver.find_element(By.XPATH, "//button[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-19yznuf r-64el8z r-1fkl15p r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']")
        login_button.click()
        driver.implicitly_wait(10)

        trends = driver.find_elements(By.XPATH, "//span[@class='css-146c3p1 r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-b88u0q r-1bymd8e']")

        trendlist= []
        for trend in trends:
            trendlist.append(trend.text)
        print(trendlist)
        if "Proxy Type" in WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.card-text"))):
            break
    except Exception:
        driver.quit()
print("Proxy Invoked")