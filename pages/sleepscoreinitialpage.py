
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SleepScoreHowWouldYouLikeToImproveYourSleepPage:

  #URL
  URL1 = 'https://onboarding.sleepio.com/sleepio/big-health#2/1'
  
  IMPROVEYOURSLEEP_TITLE = (By.CSS_SELECTOR, "label.sl-page-title")
  YOURSLEEPSCORE_HEADER = (By.CLASS_NAME, "sl-header__text")
  CHOOSE_OPTION_1 = (By.ID, 'options-id-0')
  CHOOSE_OPTION_2 = (By.ID, 'options-id-3')
  CLICK_CONTINUE = (By.CSS_SELECTOR, 'button.sl-button') #the continue button on howwouldyouliketoimproveyoursleeppage
  HOWLONGHAVEYOUHADAPROBLEM_TITLE = (By.CSS_SELECTOR, "label.sl-page-title")

  def __init__(self, browser):
    self.browser = browser

  def load_improvesleeppage(self):
    self.browser.get(self.URL1)

  def result_link_title(self):
    link = self.browser.find_element(*self.IMPROVEYOURSLEEP_TITLE)
    text = link.text
    return text

  def check_multiple_options(self):
    check_first = self.browser.find_element(*self.CHOOSE_OPTION_1)
    check_first.click()
    check_second = self.browser.find_element(*self.CHOOSE_OPTION_2)
    check_second.click()
  
  def result_header_value(self):
    header = self.browser.find_element(*self.YOURSLEEPSCORE_HEADER)
    text = header.text
    return text

  def title(self):
    return self.browser.title

  def click_continue(self):
      continue_click = self.browser.find_element(*self.CLICK_CONTINUE)
      continue_click.click()

#   def result_value(self):
#       howlonghaveyouhadaproblem_header = self.browser.find_element(*self.IMPROVEYOURSLEEP_TITLE)
#       text = header.text
#       return text

#   def check_multiple_options(self):
#     check_first = self.browser.find_element(*self.CHOOSE_OPTION_1)
#     check_first.click()
#     check_second = self.browser.find_element(*self.CHOOSE_OPTION_2)
#     check_second.click()

