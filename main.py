import base64

from selenium.webdriver.common.by import By

from register.register import Register
from register import const

with Register(executable_path=r'C:\SeleniumDrivers\chromedriver.exe') as bot:
    # bot.get_home_page()
    username = const.ACCOUNT[0][0]
    password = const.ACCOUNT[0][1]
    bot.get_login_page()
    username_input = bot.find_element(By.CSS_SELECTOR, 'input[type="text"]')
    username_input.clear()
    username_input.send_keys(username)
    password_input = bot.find_element(By.CSS_SELECTOR, 'input[type="password"]')
    password_input.clear()
    password_input.send_keys(password)
    captcha_element = bot.find_element(By.CSS_SELECTOR, 'img[src="captcha/JpegImage.aspx"]')
    img_captcha_base64 = bot.execute_async_script(
        """
        var ele = arguments[0], callback = arguments[1];
        ele.addEventListener('load', function fn(){
          ele.removeEventListener('load', fn, false);
          var cnv = document.createElement('canvas');
          cnv.width = this.width; cnv.height = this.height;
          cnv.getContext('2d').drawImage(this, 0, 0);
          callback(cnv.toDataURL('image/jpeg').substring(22));
        }, false);
        ele.dispatchEvent(new Event('load'));
        """,
        captcha_element
    )
    with open(r"temp\captcha.jpg", 'wb') as f:
        f.write(base64.b64decode(img_captcha_base64))
    