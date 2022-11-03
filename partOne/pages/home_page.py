from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    COMPOSE_BTN = (By.XPATH, "//div[contains(text(),'Compose')]")
    GMAIL_LOGO = (By.XPATH, "//img[@role='presentation']")
    TO_FIELD = (By.XPATH, "//input[@class='agP aFw']")
    SUBJECT_FIELD = (By.XPATH, "//input[@class='aoT'][@name='subjectbox']")
    BODY_FIELD = (By.XPATH, "//div[@class='Am Al editable LW-avf tS-tW']")
    SENT_BTN = (By.XPATH, "//div[@class='T-I J-J5-Ji aoO v7 T-I-atl L3']")

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def click_compose_button(self):
        print("CLick Cart Button")
        self.find_element(*self.COMPOSE_BTN).click()

    def is_home_page_displayed(self):
        print("Check if Home Page is displayed")
        try:
            self.wait_element(*self.GMAIL_LOGO)
            return True
        except TimeoutException:
            return False

    def enter_to_field(self):
        self.wait_element(*self.TO_FIELD)
        self.find_element(*self.TO_FIELD).send_keys("buulong2410992@gmail.com")

    def enter_subject_field(self):
        self.wait_element(*self.SUBJECT_FIELD)
        # self.find_element(*self.SUBJECT_FIELD).click()
        self.find_element(*self.SUBJECT_FIELD).send_keys("test")

    def enter_body_field(self):
        self.find_element(*self.BODY_FIELD).send_keys("test")

    def click_sent_button(self):
        print("CLick Sent Button")
        self.find_element(*self.SENT_BTN).click()