import pytest
import unittest
import subprocess
import requests
import time
import logging

from selenium import webdriver


logging.basicConfig(level='INFO')

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

    def test_tornado_up(self):
        baseurl = "http://localhost:8888"
        driver = self.driver
        driver.get(baseurl)
        self.assertIn("Introduction", driver.title)

    def tearDown(self):
        self.driver.close()
        self.basic_tornado.kill()

if __name__ == '__main__':
    pytest.main()
