import base64
import uuid

from selenium.webdriver import Chrome, ChromeOptions
from register import const


class Register(Chrome):
    def __init__(self, close=False, *args, **kwargs):
        options = ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.close = close
        super().__init__(executable_path=r'C:\SeleniumDrivers\chromedriver.exe', options=options, *args, **kwargs)
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.close:
            self.quit()
    
    def get_home_page(self):
        self.get(const.BASE_URL)
    
    def get_login_page(self):
        self.get(const.LOGIN_URL)
    
    def get_exam_register_page(self):
        self.get(const.EXAM_REGISTER_URL)
    
    def save_captcha_image(self, captcha_element, file_name=uuid.uuid4()):
        img_captcha_base64 = self.execute_async_script(
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
        with open(rf"..\temp\{file_name}.jpg", 'wb') as f:
            f.write(base64.b64decode(img_captcha_base64))
        