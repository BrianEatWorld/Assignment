import logging
import pytest
import unittest
import subprocess
import time
import requests

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

    def test_catchAll(self):
        baseurl = "localhost:8888/"
        # Some of these will not actually be caught by catchAllHandler, but they should all 404 so the assertion remains the same.
        missingPages = ["module.hl", "weNeedToGoDeeper.html", 'deeper/weHaveToGoDeeper.html', "deeper/deeperStill/weHaveToGoDeeper.html", "deeper/deeperStill/evenDeeperStill/weHaveToGoDeeper.html"]
        driver = self.driver
        for page in missingPages:
            driver.get(baseurl+page)
            self.assertIn("404 | Semantic UI", driver.title)

    def tearDown(self):
        self.driver.close()
        self.basic_tornado.kill()

if __name__ == '__main__':
    pytest.main()
