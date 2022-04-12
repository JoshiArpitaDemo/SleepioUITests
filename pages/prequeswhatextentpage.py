from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class WhatExtentPastMonthPage:

  URL4 = 'https://onboarding.sleepio.com/sleepio/big-health#2/4'
  DDELEMENT = (By.CSS_SELECTOR, 'select.sl-select')
  CONTINUE_BUTTON_WRAPPER = (By.CLASS_NAME, 'sl-button-wrapper')
  ERRORELEMENT = (By.CLASS_NAME, 'sl-general-error')


  def __init__(self, browser):
     self.browser = browser

  def load(self):
     self.browser.get(self.URL4)

  def click_dropdown(self):
     click_the_dropdown = self.browser.find_element(*self.DDELEMENT)
     click_the_dropdown.click()

  def dropdown_selections(self):
     click_the_dropdown = self.browser.find_element(*self.DDELEMENT)
     click_the_dropdown.send_keys("Somewhat")

  def click_button_wrapper(self):
     continue_click = self.browser.find_element(*self.CONTINUE_BUTTON_WRAPPER)
     continue_click.click()

  def error_message_shown(self):
      message = self.browser.find_element(*self.ERRORELEMENT)
      msg = message.text
      assert "Please answer all the questions before continuing." == msg 