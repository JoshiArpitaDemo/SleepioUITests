"""
These tests cover the navigation from the "How would you like to improve your sleep?" Page to the next page "How long have you had a problem with your sleep?"
"""
import pytest
import time
from pages.sleepscoreinitialpage import SleepScoreHowWouldYouLikeToImproveYourSleepPage
from pages.getstarted import SleepioLandingPage


@pytest.mark.usefixtures("browser")
def test_navigation_from_improveyoursleep_page(browser):
     initial_page = SleepScoreHowWouldYouLikeToImproveYourSleepPage(browser)
     landing_page = SleepioLandingPage(browser)
   

#Given the How would you like to improve your sleep page is displayed
     initial_page.load_improvesleeppage() #this redirects to the main page
     #landing_page.load()

#When the user clicks any of the checkbox
     landing_page.click()
     initial_page.check_multiple_options()

#And the user clicks continue
     initial_page.click_continue()


#Then the `How long have you had a problem with your sleep?` page appears
     assert "How long have you had a problem with your sleep?" in initial_page.result_link_title()
