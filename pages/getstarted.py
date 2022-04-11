from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SleepioLandingPage:

  #URL
  
  URL = 'https://onboarding.sleepio.com/sleepio/big-health#1/1'

  #Locators

  GETSTARTED_BUTTON = (By.CSS_SELECTOR, 'button.sl-button')

  #Initializer

  def __init__(self, browser):
    self.browser = browser

  #Interaction Methods
  def load(self):
    self.browser.get(self.URL)

  def click(self):
    search_get_started = self.browser.find_element(*self.GETSTARTED_BUTTON)
    search_get_started.click()
