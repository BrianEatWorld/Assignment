import nose
import unittest
import subprocess

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class semanticMain(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		try:
			self.basic_tornado = subprocess.Popen(["python","./assignment/basic.py"])
		except:
			logging.info("error occured on start, killing")
			self.basic_tornado.kill()

	def test_Main(self):
		baseurl = "localhost:8888"
		driver = self.driver
		driver.get(baseurl)
		self.assertIn("Introduction", driver.title)
		driver.find_element_by_css_selector("a.ui:nth-child(4)").click()
		driver.find_element_by_css_selector("div.item:nth-child(5) > a:nth-child(1) > b:nth-child(1)").click()
		self.assertIn("UI Elements", driver.title)
		driver.get(baseurl)
		driver.find_element_by_css_selector("a.ui:nth-child(4)").click()
		driver.execute_script("document.getElementById('menu').children[4].children[0].setAttribute('href','Element5.html')");
		driver.find_element_by_css_selector("div.item:nth-child(5) > a:nth-child(1) > b:nth-child(1)").click()
		self.assertIn("404 | Semantic UI", driver.title)

	def tearDown(self):
		self.driver.close()
		self.basic_tornado.kill()

if __name__ == '__main__':
    nose.main()