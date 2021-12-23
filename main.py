from selenium.webdriver.common.by import By

from register.register import Register
from register import const

with Register() as bot:
    # bot.get_home_page()
    username = const.ACCOUNT[0][0]
    password = const.ACCOUNT[0][1]
    bot.set_window_rect(0, 0, 200, 800)
    bot.get_login_page()
    username_input = bot.find_element(By.CSS_SELECTOR, 'input[type="text"]')
    username_input.clear()
    username_input.send_keys(username)
    password_input = bot.find_element(By.CSS_SELECTOR, 'input[type="password"]')
    password_input.clear()
    password_input.send_keys(password)
    # captcha_element = bot.find_element(By.CSS_SELECTOR, 'img[src="captcha/JpegImage.aspx"]')
    # bot.save_captcha_image(captcha_element)
    captcha_input = bot.find_element(By.CSS_SELECTOR, 'input[type="text"][id="ctl03_tbCaptcha"]')
    login_button = bot.find_element(By.ID, 'ctl03_btnLogin')
    captcha = input('Pleas enter captcha:')
    captcha_input.send_keys(captcha)
    bot.set_window_size(800, 800)
    login_button.click()
    # register_page_link = bot.find_element(By.LINK_TEXT, 'ثبت نام آزمون')
    # register_page_link.click()
    bot.execute_script("window.open('');")
    bot.switch_to.window(bot.window_handles[1])
    bot.get_exam_register_page()
    