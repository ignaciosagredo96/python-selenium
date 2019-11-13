from selenium import webdriver


def before_scenario(context, scenario):
    if 'web' in context.tags:
        context.driver = webdriver.Chrome("C:\Program Files (x86)\Python38-32\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe")
        context.driver.maximize_window()
        context.driver.implicitly_wait(10)


def after_scenario(context, scenario):
    if 'web' in context.tags:
        context.driver.quit()
