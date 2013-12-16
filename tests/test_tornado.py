import pytest
import unittest
import subprocess
import requests
import sys
import time

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


	def test_wait_for_http(url,timeout,interval):
		logging.info("Waiting for 2XX response from:",url)
		for _ in range(int(timeout/interval)):
			try:
				assert str(requests.get(url).status_code)[0]=='2'
				return
			except:
				sys.stdout.write('.')
				sys.stdout.flush()
				time.sleep(int(interval))
		raise Exception('HTTP Timed Out on',url)

	def test_tornado_up(self):
		baseurl = "localhost:8888"
		driver = self.driver
		driver.get(baseurl)
		self.assertIn("Introduction", driver.title)

	def tearDown(self):
		self.driver.close()
		self.basic_tornado.kill()

if __name__ == '__main__':
    nose.main()