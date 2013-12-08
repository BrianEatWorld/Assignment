import nose
import unittest
import subprocess

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Because this is testing rendering, it may be a good idea to have it run using multiple drivers.
# I.E. Have a Chrome and FIrefox version of the test.

class semanticMain(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		try:
			self.basicTornado = subprocess.Popen(["python","./assignment/basic.py"])
		except:
			logging.info("error occured on start, killing")
			self.basicTornado.kill()

	def test_Download(self):
		baseurl = "localhost:8888/"
		driver = self.driver
		driver.get(baseurl)
		#First test checks to see that the "Download" for "Build" works properly
		self.assertIn("Introduction", driver.title)
		driver.find_element_by_css_selector("a.red").click()
		try:
			alert = self.driver.switch_to_alert()
			alExists = True
		except:
			alExists = False

		alert = self.assertTrue(alExists)


	def tearDown(self):
		self.driver.close()
		self.basicTornado.kill()

if __name__ == '__main__':
    nose.main()