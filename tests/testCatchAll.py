import nose
import unittest
import subprocess

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class semanticMain(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		try:
			self.basicTornado = subprocess.Popen(["python","./assignment/basic.py"])
		except:
			logging.info("error occured on start, killing")
			self.basicTornado.kill()

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
		self.basicTornado.kill()

if __name__ == '__main__':
    nose.main()