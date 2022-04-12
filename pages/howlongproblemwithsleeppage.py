from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class HowLongProblemWithSleepPage:

  URL2 = 'https://onboarding.sleepio.com/sleepio/big-health#2/2'
  DDELEMENT = (By.CSS_SELECTOR, 'select.sl-select')
  CONTINUE_CLICK = (By.CSS_SELECTOR, 'button.sl-button  ')

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
  
  def list_all_selections(self):
     click_the_dropdown = self.browser.find_element(*self.DDELEMENT)
     element = Select(self.browser.find_element(By.ID, "id-9")).options
     dd = Select(click_the_dropdown)
     dd1 = dd.select_by_index(1)
     time.sleep(3)
     dd2 = dd.select_by_visible_text("A week or less")
     time.sleep(3)
     dd3 = dd.select_by_value("2")
     time.sleep(3)

  def continue_click(self):
     continue_click = self.browser.find_element(*self.CONTINUE_CLICK)
     continue_click.click()