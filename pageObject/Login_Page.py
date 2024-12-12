from selenium.webdriver.common.by import By


class LoginPage:
    text_username_Xpath="//input[@id='username']"
    text_password_Xpath="//input[@id='password']"
    click_login__button_Xpath= "//button[@id='loginButton']"
    click_logout_button_Xpath= "//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver=driver

    def Enter_username(self,name):
        self.driver.find_element(By.XPATH,self.text_username_Xpath).send_keys(name)

    def Enter_password(self,password):
        self.driver.find_element(By.XPATH,self.text_password_Xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH,self.click_login__button_Xpath).click()

    def click_logout_button(self):
        self.driver.find_element(By.XPATH,self.click_logout_button_Xpath).click()