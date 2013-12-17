import pytest
import unittest
import subprocess
import requests
import time
import logging
import sys

from selenium import webdriver


class tornadoTestMain(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        try:
            self.basic_tornado = subprocess.Popen(["python", "./assignment/basic.py"])

        except:
            logging.info("error occured on start, killing")
            self.basic_tornado.kill()

    def test_wait_for_http(self):
        url = "localhost:8888"
        timeout = 2
        interval = 1
        logging.info("Waiting for 2XX response from:", url)
        for _ in range(int(timeout/interval)):
            try:
                sys.stdout.write("successfully started")
                assert str(requests.get(url).status_code)[0] == '2'
                return
            except:
                sys.stdout.write('waiting')
                sys.stdout.write('.')
                sys.stdout.flush()
                time.sleep(int(interval))

    def test_tornado_up(self):
        baseurl = "localhost:8888"
        driver = self.driver
        driver.get(baseurl)
        self.assertIn("Introduction", driver.title)

    def tearDown(self):
        self.driver.close()
        self.basic_tornado.kill()

if __name__ == '__main__':
    pytest.tornadoTestMain()
