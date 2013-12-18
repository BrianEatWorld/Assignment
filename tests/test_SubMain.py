import logging
import pytest
import unittest
import subprocess
import time
import requests

from selenium import webdriver


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

    def test_subMain(self):
        baseurl = "localhost:8888"
        driver = self.driver
        driver.get(baseurl)
        self.assertIn("Introduction", driver.title)
        driver.find_element_by_css_selector('a.ui:nth-child(4)').click()
        # driver.find_element_by_css_selector('div.item:nth-child(6) > div:nth-child(2) > a:nth-child(1)').click()
        driver.find_element_by_link_text("Breadcrumb").click()
        self.assertIn("Breadcrumb | Semantic UI", driver.title)
        driver.get(baseurl)
        driver.find_element_by_css_selector("a.ui:nth-child(4)").click()
        driver.execute_script("document.getElementById('menu').children[4].children[0].setAttribute('href','Element5.html')")
        driver.find_element_by_css_selector("div.item:nth-child(5) > a:nth-child(1) > b:nth-child(1)").click()
        self.assertIn("404 | Semantic UI", driver.title)

    def tearDown(self):
        self.driver.close()
        self.basic_tornado.kill()

if __name__ == '__main__':
    pytest.main()
