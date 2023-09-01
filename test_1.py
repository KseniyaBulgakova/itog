import time
import yaml
import logging

from testpage import OperationsHelper

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
name = testdata["username"]
passwd = testdata["password"]


def test_step_1(browser):
    logging.info("Test 1 Start")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_step_2(browser):
    logging.info("Test 2 Start")
    testpage = OperationsHelper(browser)
    testpage.enter_login(name)
    testpage.enter_pass(passwd)
    testpage.click_login_button()
    assert testpage.get_user_text() == f"Hello, {name}"


def test_step_3(browser):
    logging.info("Test 3 Start")
    testpage = OperationsHelper(browser)
    testpage.click_new_post_btn()
    testpage.enter_title("testtitle")
    testpage.enter_content("testcontent")
    testpage.enter_description("testdesc")
    testpage.click_save_btn()
    time.sleep(2)
    assert testpage.get_res_text() == "testtitle"


def test_step_4(browser):
    logging.info("Test 4 Start")
    testpage = OperationsHelper(browser)
    testpage.click_contact_link()
    time.sleep(2)
    testpage.enter_contact_name("testname")
    testpage.enter_contact_mail("test@test.ru")
    testpage.enter_contact_content("testcontactcontent")
    time.sleep(2)
    testpage.click_contact_send_btn()
    time.sleep(3)
    assert testpage.get_alert() == "Form successfully submitted"