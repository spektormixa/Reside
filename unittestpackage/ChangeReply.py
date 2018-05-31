from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class ChangeRepl(unittest.TestCase):

    def test_change_reply(self):
        base_url = "https://github.com/settings/replies"
        driver = webdriver.Firefox()
        driver.get(base_url)
        driver.maximize_window()
        driver.implicitly_wait(5)
        login_username = "residetest"
        login_password = "QWErty654321"

        # Login to GIT
        login = driver.find_element_by_id("login_field")
        login.click()
        login.send_keys(login_username)
        password = driver.find_element_by_id("password")
        password.click()
        password.send_keys(login_password)

        sign_in = driver.find_element(By.XPATH, "//input[@value = 'Sign in']")
        sign_in.click()
        # Adding time just for visibility
        time.sleep(1)

        # Creating test reply
        reply_title = driver.find_element_by_id("saved-reply-title-field")
        reply_title.click()
        reply_title.send_keys("Reside test reply")

        # Changing style of header
        header_style = driver.find_element(By.XPATH, "//button[@aria-label = 'Add header text']")
        header_style.click()
        style_type = driver.find_element(By.XPATH, "//button[@class='dropdown-item dropdown-header3']")
        style_type.click()

        #Adding text to reply
        textarea = driver.find_element_by_id("comment_body_1")
        textarea.click()
        textarea.send_keys("This is a test comment for positive test case of replies function in GIT")

        # Add saved reply
        add_reply = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
        add_reply.click()
        print("Saved reply added")
        # Adding time just for visibility
        time.sleep(1)

        # Verifying that reply is actually present
        reply_check = driver.find_elements(By.XPATH, "//span[contains(text(),'Reside test reply')]")
        if reply_check is None:
            print("Reply is not added")
        else:
            print("Reply is added and visible")

        # Changing existing reply
        reply_change = driver.find_element_by_xpath(
            " //div[@class ='listgroup']//button[@aria-label ='Edit reply']")
        reply_change.click()
        input_field = driver.find_element_by_id("saved-reply-title-field")
        input_field.clear()
        input_field.send_keys("This is a title of Reside test")

        # Submit changes
        update_reply = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
        update_reply.click()

        # Verifying that reply title is changed
        reply_title = driver.find_elements(By.XPATH, "//span[contains(text(),'This is a title')]")
        if reply_check is None:
            print("Reply is not changed")
        else:
            print("Reply is changed and visible")
        # Adding time just for visibility
        time.sleep(2)

        driver.close()

if __name__ == '__main__':
    unittest.main()

