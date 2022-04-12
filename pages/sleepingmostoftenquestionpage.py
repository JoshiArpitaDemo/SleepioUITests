from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class WhatStopsFromSleepingMostOftenPage:

  URL3 = 'https://onboarding.sleepio.com/sleepio/big-health#2/3'
  RADIOELEMENT_FIRST = (By.ID, 'options-id-0')
  RADIOELEMENT_SECOND = (By.ID, 'options-id-1')
  CONTINUE_CLICK = (By.CSS_SELECTOR, 'button.sl-button  ')

  def __init__(self, browser):
     self.browser = browser

  def load(self):
     self.browser.get(self.URL3)

  def select_first_radio_button(self):
     select_first_radio = self.browser.find_element(*self.RADIOELEMENT_FIRST)
     select_first_radio.click()


  def select_the_second_radio_button(self):
      select_second_radio = self.browser.find_element(*self.RADIOELEMENT_SECOND)
      select_second_radio.click()

  def click_continue(self):
      continue_click = self.browser.find_element(*self.CONTINUE_CLICK)
      continue_click.click()

  def the_first_option_greysout(self):
      first_option = self.browser.find_element(*self.RADIOELEMENT_FIRST)
      assert(first_option.is_enabled()) == True
      assert(first_option.is_selected()) == False
   
  def the_second_option_remains_selected(self):
      second_option = self.browser.find_element(*self.RADIOELEMENT_SECOND)
      assert(second_option.is_enabled()) == True
      assert(second_option.is_selected()) == True