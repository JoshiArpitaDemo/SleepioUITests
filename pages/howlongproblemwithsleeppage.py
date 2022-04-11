from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class HowLongProblemWithSleepPage:

  URL2 = 'https://onboarding.sleepio.com/sleepio/big-health#2/2'
  DDELEMENT = (By.CSS_SELECTOR, 'select.sl-select')

  def __init__(self, browser):
     self.browser = browser

  def load(self):
     self.browser.get(self.URL2)

  def click_dropdown(self):
     click_the_dropdown = self.browser.find_element(*self.DDELEMENT)
     click_the_dropdown.click()

  def dropdown_selections(self):
      click_the_dropdown = self.browser.find_element(*self.DDELEMENT)
      click_the_dropdown.send_keys("A week or less")
