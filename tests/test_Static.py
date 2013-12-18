import logging
import pytest
import unittest
import subprocess
import time
import requests

from selenium import webdriver


# Because this is testing rendering, it may be a good idea to have it run using multiple drivers.
# I.E. Have a Chrome and FIrefox version of the test.
class main(unittest.TestCase):

    def setUp(self):
        url = "http://localhost:8888"
        timeout = 10
        interval = 1
        self.basic_tornado = subprocess.Popen(["start-tornado"])
        logging.info("Waiting for 2XX response from:", url)
        for _ in range(int(timeout/interval)):
            try:
                logging.info('attempting request')
                assert str(requests.get(url))
                self.driver = webdriver.Firefox()
                return
            except:
                logging.info('request failed')
                time.sleep(int(interval))
        logging.info('Unable to access tornado, killing. Check settings and try again.')
        self.basic_tornado.kill()

    def test_Download(self):
        baseurl = "localhost:8888/"
        driver = self.driver
        driver.get(baseurl)
        #First test checks to see that the "Download" for "Build" works properly
        self.assertIn("Introduction", driver.title)
        driver.find_element_by_css_selector("a.red").click()
        self.driver.switch_to_alert()
        try:
            self.driver.switch_to_alert()
            alExists = True
        except NoAlertPresentException:
            alExists = False

        self.assertTrue(alExists)

    def tearDown(self):
        self.driver.close()
        self.basic_tornado.kill()

if __name__ == '__main__':
    pytest.main()
