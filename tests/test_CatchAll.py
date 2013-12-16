import logging
import pytest
import unittest
import subprocess

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class semanticCatchAll(unittest.TestCase):

	def setUp(self):
		try:
			self.driver = webdriver.Firefox()
			self.basic_tornado = subprocess.Popen(["python","./assignment/basic.py"])
			logging.info(''.join(["Tornado PID: ",basic_tornado.pid])) 
		except:
			logging.info("error occured on start, killing")
			self.basic_tornado.kill()

	def test_catchAll(self):
		baseurl = "localhost:8888/"
		# Some of these will not actually be caught by catchAllHandler, but they should all 404 so the assertion remains the same.
		missingPages = ["module.hl","weNeedToGoDeeper.html",'deeper/weHaveToGoDeeper.html',"deeper/deeperStill/weHaveToGoDeeper.html","deeper/deeperStill/evenDeeperStill/weHaveToGoDeeper.html"]
		driver = self.driver
		for page in missingPages:
				driver.get(baseurl+page)
				self.assertIn("404 | Semantic UI", driver.title)

	def tearDown(self):
		self.driver.close()
		self.basic_tornado.kill()

if __name__ == '__main__':
    pytest.main()