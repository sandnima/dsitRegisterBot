from selenium.webdriver import Chrome
from register import const


class Register(Chrome):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def get_home_page(self):
        self.get(const.BASE_URL)
        