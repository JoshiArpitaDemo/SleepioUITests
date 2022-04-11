
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SleepScoreHowWouldYouLikeToImproveYourSleepPage:
  
  IMPROVEYOURSLEEP_TITLE = (By.CSS_SELECTOR, "label.s1-page-title")
  #YOURSLEEPSCORE_HEADER = (By.)

  def __init__(self, browser):
    self.browser = browser

  def result_link_title(self):
    link = self.browser.find_element(*self.IMPROVEYOURSLEEP_TITLE)
    title = link.title
    return title
  
#   def search_input_value(self):
#     # TODO
#     return ""

  def title(self):
    return self.browser.title