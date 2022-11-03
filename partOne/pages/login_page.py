from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import users
from selenium.common.exceptions import TimeoutException


class LoginPage(BasePage):
    LOGIN_BTN = (By.XPATH, "//a[normalize-space()='Đăng nhập']")
    EMAIL_FIELD = (By.XPATH, "//input[@id='identifierId']")
    PASSWORD = (By.XPATH, "//input[@name='Passwd']")
    NEXT_BTN = (By.XPATH, "//span[normalize-space()='Next']")
    CONFIRM_LOGIN_BTN = (By.XPATH, "//div[@class='login-box']//input[@id='login-button']")
    CREATE_ACC_BTN = (By.XPATH, "//span[normalize-space()='Create account']")

    test1 = (By.XPATH, "//a[normalize-space()='Log in']")
    test2 = (By.XPATH, "//button[normalize-space()='Log in with Google']")
    test3 = (By.XPATH, "//span[normalize-space()='Tiếp theo']")

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)  # Python2 version

    def is_login_page_displayed(self):
        print("Check if Login Page is displayed")
        try:
            self.wait_element(*self.EMAIL_FIELD)
            self.wait_element(*self.NEXT_BTN)
            self.wait_element(*self.CREATE_ACC_BTN)
            return True
        except TimeoutException:
            return False

    def click_login_btn(self):
        self.wait_element(*self.LOGIN_BTN)
        self.find_element(*self.LOGIN_BTN).click()

    def enter_email(self, email):
        self.find_element(*self.EMAIL_FIELD).send_keys(email)

    def click_next_btn(self):
        self.wait_element(*self.NEXT_BTN)
        self.find_element(*self.NEXT_BTN).click()

    def enter_password(self, password):
        self.wait_element(*self.PASSWORD)
        self.find_element(*self.PASSWORD).send_keys(password)

    def click_to_login_button(self):
        self.find_element(*self.LOGIN_BTN).click()

    def login(self, user):
        user = users.get_user(user)
        print(user)
        self.enter_email(user["email"])
        sleep(3)
        self.click_next_btn()
        sleep(3)
        self.enter_password(user["password"])
        sleep(3)
        self.click_next_btn()
