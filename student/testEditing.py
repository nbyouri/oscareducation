# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

login = "eleve.eleve"
pwd = "eleve"

loginProf = "prof"
pwdProf = "prof"


# Simple question
tests = [{"nomDuTest" : "Test de Pythagore", "enonce" : "Soit un triangle rectangle dont un est des côtés adjacents est de 3cm, et l'autre de 4 cm, combien de cm mesure l'hypothénuse ? (Réponse uniquement en nombres)","answers":"5"}]

# Double question
tests2 = []

# Placeholders
tests3 = []


class TestEditing(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(2)
        self.base_url = "http://127.0.0.1:8000/"
        self.login = login
        self.pwd = pwd

    def testPersistance(self):
        driver = self.driver
        driver.get(self.base_url + "accounts/usernamelogin/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(loginProf)
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(pwdProf)
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        driver.find_element_by_xpath("//a[@href='/professor/lesson/134/']").click()
        driver.get("http://127.0.0.1:8000/professor/lesson/134/test/add/")
        driver.find_element_by_xpath("//a[@href='/professor/lesson/134/test/online/add/']").click()
        print(driver.current_url)
        print(driver.find_element_by_id("test_name").text)
        driver.find_element_by_id("test_name").send_keys("Test de Pythagore")
        driver.find_element_by_id("addSkillToTestButtonForStage9").click()
        elem = driver.find_element_by_id("test_name")

        try:
            driver.find_element_by_id("id_create_test_button").click()

        except:
            print("fail")




        # The click doesn't works
        elem.send_keys(Keys.ENTER)
        driver.execute_script('document.getElementById("id_create_test_button").click();')
        print(driver.current_url)
        wait = WebDriverWait(driver, 10)
        print(driver.current_url)


        # We pass directly to the question form creation.
        driver.get(self.base_url + "professor/exercices/validation_form/#?for_test_exercice=14&code=S41eII")

        driver.find_element_by_id("exercice-html")
        elem = driver.find_element_by_id("exercice-html")
        elem.send_keys("Enonce")
        #elem2 = driver.find_element_by_class_name("form-control ng-pristine ng-invalid ng-invalid-required")
        #elem.send_keys("Question")
        """driver.find_element_by_id("blank-text").clear()
        driver.find_element_by_id("blank-text").send_keys("Un")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_id("blank-text").clear()
        driver.find_element_by_id("blank-text").send_keys(u"Un #[1]# possède un diamètre, un rayon et un")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_id("blank-text").clear()
        driver.find_element_by_id("blank-text").send_keys(u"Un #[1]# possède un diamètre, un rayon et un #[2]#.")
        driver.find_element_by_id("blank-text").clear()
        driver.find_element_by_id("blank-text").send_keys("Un")

        """

        Select(driver.find_element_by_xpath("//li/div/div/div/select")).select_by_visible_text(u"Question à trous")


        #self.assertEqual(1,1)
        driver.find_element_by_css_selector("button.btn.btn-success").send_keys(Keys.ENTER)

        wait = WebDriverWait(driver, 30)
        driver.implicitly_wait(1000)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


