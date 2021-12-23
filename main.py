from register.register import Register

with Register(executable_path=r'C:\SeleniumDrivers\chromedriver.exe') as bot:
    bot.get_home_page()
