import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAddRemoveElements(unittest.TestCase):
    
    def setUp(self):
      self.driver = webdriver.Chrome(ChromeDriverManager().install())
      URL = "http://the-internet.herokuapp.com/dynamic_controls"
      self.driver.get(URL)
    
    def tearDown(self):
      pass
      #self.driver.quit()

    def testRemove(self):
      driver = self.driver



if __name__ == '__main__':
   unittest.main()