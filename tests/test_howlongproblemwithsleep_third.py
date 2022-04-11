"""
These tests cover the navigation from the "How long have you had a problem with your sleep?" Page to the next page "Which of the following stops you from sleeping most often?"
"""
from selenium.webdriver.support.ui import Select
import pytest
import time
from pages.sleepscoreinitialpage import SleepScoreHowWouldYouLikeToImproveYourSleepPage
from pages.getstarted import SleepioLandingPage
from pages.howlongproblemwithsleeppage import HowLongProblemWithSleepPage


@pytest.mark.usefixtures("browser")
def test_navigation_from_howlongproblemwithsleep_page(browser):
     initial_page = SleepScoreHowWouldYouLikeToImproveYourSleepPage(browser)
     landing_page = SleepioLandingPage(browser)
     problemwithsleep_page = HowLongProblemWithSleepPage(browser)

#Given the `How long have you had a problem with your sleep?` page is displayed
     initial_page.load_improvesleeppage()
     landing_page.click()
     initial_page.check_multiple_options()
     initial_page.click_continue()


#When the `Please Select` dropdown menu is clicked
     problemwithsleep_page.click_dropdown()

#Then dropdown options appear as expected (Trying out Select class)
def list_all_selections(browser):
     click_the_dropdown = self.browser.find_element(*self.DDELEMENT)
     element = Select(self.browser.find_element(By.ID, "id-9")).options
     dd = Select(click_the_dropdown)
     dd1 = dd.select_by_index(1)
     dd2 = dd.select_by_visible_text("A week or less")
     dd3 = dd.select_by_value("2")
     assert "I don't have a problem" == dd1
     assert "A week or less" == dd2
     assert "2-4 weeks" == dd3