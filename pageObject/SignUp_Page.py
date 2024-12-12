from selenium.webdriver.common.by import By


class signUp_class:

    text_username_Xpath="//input[@id='username']"
    text_password_Xpath="//input[@id='password']"
    text_email_Xpath="//input[@id='email']"
    text_phone_Xpath="//input[@id='phone']"
    click_Createuser_button_Xpath="//button[@id='createUserButton']"
    success_message_xpath ="//div[@id='successMessage']"
    def __init__(self,driver):
        self.driver=driver

    def Enter_username(self,name):
        self.driver.find_element(By.XPATH,self.text_username_Xpath).send_keys(name)

    def Enter_password(self,password):
        self.driver.find_element(By.XPATH,self.text_password_Xpath).send_keys(password)

    def Enter_email(self,email):
        self.driver.find_element(By.XPATH,self.text_email_Xpath).send_keys(email)

    def Enter_phone(self,phone):
        self.driver.find_element(By.XPATH,self.text_phone_Xpath).send_keys(phone)

    def click_Createuser_button(self):
        self.driver.find_element(By.XPATH,self.click_Createuser_button_Xpath).click()

    def verify_success_message(self):
        try:
            msg = self.driver.find_element(By.XPATH,self.success_message_xpath)
            print(msg.text)
            return "SignUp Pass"
        except:
            return "SignUp Fail"


