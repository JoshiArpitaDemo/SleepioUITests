from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class MultipleScreenPages:

  URL5 = 'https://onboarding.sleepio.com/sleepio/big-health#2/5'
  DDELEMENT = (By.CSS_SELECTOR, 'select.sl-select')
  CLICK_CONTINUE = (By.CSS_SELECTOR, 'button.sl-button')
  RADIOELEMENT_SECOND = (By.ID, 'options-id-1')
  MONTH_DROPDOWN = (By.ID, 'select-month')
  DAY_DROPDOWN = (By.ID, 'select-day' )
  YEAR_DROPDOWN = (By.ID, 'select-year')
  PRODUCTIVITY_TXT = (By.CLASS_NAME, 'sl-input-number ')
  GUIDE_TXT_TITLE = (By.CLASS_NAME, 'sl-page-title')
  RADIOELEMENT_FIRST = (By.ID, 'options-id-0')
  FIRST_NAME = (By.NAME, 'first_name')
  LAST_NAME = (By.NAME, 'last_name')
  EMAIL = (By.NAME, 'email')
  PASSWORD = (By.NAME, 'password')
  FIRST_CHECKBOX = (By.XPATH, '//*[@id="sl-flow"]/div[3]/div/div/div/div/form/div[5]/input')
  SECOND_CHECKBOX = (By.XPATH, '//*[@id="sl-flow"]/div[3]/div/div/div/div/form/div[6]/input')
  SUBMIT_BUTTON = (By.CLASS_NAME, 'sl-button  ')
  SLEEP_SCORE_PAGE = (By.CLASS_NAME, 'sl-score')

  def __init__(self, browser):
     self.browser = browser

  def load(self):
     self.browser.get(self.URL5)

  def click_dropdown(self):
     click_the_dropdown = self.browser.find_element(*self.DDELEMENT)
     click_the_dropdown.click()

  def dropdown_selections(self):
     click_the_dropdown = self.browser.find_element(*self.DDELEMENT)
     click_the_dropdown.send_keys("2 nights")

  def dropdown_selections_control(self):
     click_the_dropdown = self.browser.find_element(*self.DDELEMENT)
     click_the_dropdown.send_keys("Sometimes")

  def click_continue(self):
      continue_click = self.browser.find_element(*self.CLICK_CONTINUE)
      continue_click.click()

  def dropdown_selections_strugglepage(self):
      click_the_dropdown = self.browser.find_element(*self.DDELEMENT)
      click_the_dropdown.send_keys("Slight chance")

  def select_the_second_radio_button(self):
      select_second_radio = self.browser.find_element(*self.RADIOELEMENT_SECOND)
      select_second_radio.click()

  def dob_inputs(self):
      click_the_month_dropdown = self.browser.find_element(*self.MONTH_DROPDOWN)
      click_the_month_dropdown.send_keys("January")
      click_the_day_dropdown = self.browser.find_element(*self.DAY_DROPDOWN)
      click_the_day_dropdown.send_keys("2")
      click_the_year_dropdown = self.browser.find_element(*self.YEAR_DROPDOWN)
      click_the_year_dropdown.send_keys("2002")

  def dropdown_employment(self):
      click_the_dropdown = self.browser.find_element(*self.DDELEMENT)
      click_the_dropdown.send_keys("Employed full-time")

  def dropdown_productivity_first(self):
      click_the_dropdown = self.browser.find_element(*self.DDELEMENT)
      click_the_dropdown.send_keys("60%")

  def dropdown_productivity_second(self):
      click_the_textbox = self.browser.find_element(*self.PRODUCTIVITY_TXT)
      click_the_textbox.send_keys("10")

  def assert_guide_page(self):
      guide_title = self.browser.find_element(*self.GUIDE_TXT_TITLE)
      text = guide_title.text
      assert "Which of the following expert guides might be of interest to you?" == text

  def sign_up_details(self):
      first_name = self.browser.find_element(*self.FIRST_NAME)
      first_name.send_keys("TEST")
      last_name = self.browser.find_element(*self.LAST_NAME)
      last_name.send_keys("USER")
      email = self.browser.find_element(*self.EMAIL)
      email.send_keys("tstuser4@gmail.com")
      password = self.browser.find_element(*self.PASSWORD)
      password.send_keys("AtSJwin98$11")
      click_the_checkbox = self.browser.find_element(*self.FIRST_CHECKBOX)
      click_the_checkbox.click()
      click_the_second_checkbox = self.browser.find_element(*self.SECOND_CHECKBOX)
      click_the_second_checkbox.click()
      time.sleep(8)
      submit_click = self.browser.find_element(*self.SUBMIT_BUTTON)
      submit_click.click()
      time.sleep(5)
    
  def assert_final_page(self):
      sleep_score_final = self.browser.find_element(*self.SLEEP_SCORE_PAGE)
      text = sleep_score_final.text
      assert "6.25 / 10" in text


