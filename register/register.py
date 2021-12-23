from selenium.webdriver import Chrome
from register import const


class Register(Chrome):
    def __init__(self, close=False, *args, **kwargs):
        self.close = close
        super().__init__(*args, **kwargs)
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.close:
            self.quit()
    
    def get_home_page(self):
        self.get(const.BASE_URL)
    
    def get_login_page(self):
        self.get(const.LOGIN_URL)
        