import os.path
import time
from setting.env import env_setting


# 나중에 하기 버튼
def later_button(driver):
    # 나중에 하기1
    later_1 = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/div/div/div/div/button')
    later_1.click()
    time.sleep(3)

    # 나중에 하기2
    later_2 = driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
    later_2.click()
    time.sleep(2)


def login(driver):
    time.sleep(2)

    env_setting()
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
    input_id.clear()
    input_id.send_keys(email)

    input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
    input_pw.clear()
    input_pw.send_keys(password)

    time.sleep(5)

    input_pw.submit()

    time.sleep(5)

    later_button(driver)  # 나중에 하기 버튼
