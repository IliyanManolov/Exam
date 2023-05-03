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
      self.assertIn('dynamic_controls', driver.current_url)
      opening_page = "opening_page.png"
      driver.save_screenshot(opening_page)

      checkbox = driver.find_element(By.ID, 'checkbox')
      self.assertTrue(checkbox)

      remove_button = driver.find_element(By.XPATH, '//*[@id="checkbox-example"]/button')
      self.assertTrue(remove_button)
      remove_button.click()
      remove_button_page = "remove_button_pressed.png"
      driver.save_screenshot(remove_button_page)

      add_button_appear = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkbox-example"]/button')))
      time.sleep(5)
      add_button_page = "add_button_page.png"
      driver.save_screenshot(add_button_page)
      self.assertTrue(add_button_appear)

      add_button = driver.find_element(By.XPATH, '//*[@id="checkbox-example"]/button')
      self.assertTrue(add_button)
      time.sleep(5)
      add_button.click()
      add_button_pressed = "add_button_pressed.png"
      driver.save_screenshot(add_button_pressed)

      checkbox_reappear = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'checkbox')))
      checkbox_reappear_page = "checkbox_reappear_page.png"
      driver.save_screenshot(checkbox_reappear_page)
      self.assertTrue(checkbox_reappear)



if __name__ == '__main__':
   unittest.main()