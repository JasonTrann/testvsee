import unittest

from tests.base_test import BaseTest
from pages.home_page import *
from pages.login_page import *
from time import sleep


class TestSignInPage(BaseTest):

    def test_sign_in(self):
        # NOTE: have to wait between each step to prevent google from blocking
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)

        login_page.login("test")
        home_page.is_home_page_displayed()
        home_page.click_compose_button()
        sleep(3)
        home_page.enter_to_field()
        sleep(3)
        home_page.enter_subject_field()
        sleep(3)
        home_page.enter_body_field()
        sleep(3)
        home_page.click_sent_button()
        sleep(10)
