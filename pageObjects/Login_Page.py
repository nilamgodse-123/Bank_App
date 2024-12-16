from selenium.webdriver.common.by import By


class LoginPage:
    text_username_Xpath="//input[@id='username']"
    text_password_Xpath="//input[@id='password']"
    click_login_button_xpath= "//button[@id='loginButton']"
    click_logout_button_Xpath= "//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver=driver

    def EnterUserName(self,name):
        self.driver.find_element(By.XPATH,self.text_username_Xpath).send_keys(name)

    def EnterPassword(self,password):
        self.driver.find_element(By.XPATH,self.text_password_Xpath).send_keys(password)

    def ClickLoginButton(self):
        self.driver.find_element(By.XPATH,self.click_login_button_xpath).click()

    def click_logout_button(self):
        self.driver.find_element(By.XPATH,self.click_logout_button_Xpath).click()