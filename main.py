import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AppiumTest(unittest.TestCase):
    dc = {}
    driver = None

    def setUp(self):
        self.dc['app'] = "https://github.com/Puttajunjaiah/investorai-cryptos/raw/main/src/app/InvestorAiCrypto_1.0.7.apk"
        self.dc['platformName'] = 'Android'
        self.dc['automationName'] = 'UiAutomator2'
        self.dc['deviceName'] = 'Android Emulator'
        self.dc['appPackage'] = "com.investorai.crypto"
        self.dc['appActivity'] = "com.investorai.applauncher.presentation.MainActivity"
        self.dc['adbExecTimeout'] = 30000

        # Creating the Driver by passing Desired Capabilities.
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dc)

    def testInvestorAIApp(self):
        driver = self.driver
        wait = WebDriverWait(driver, 60)
        get_started_link = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.investorai.crypto:id/btn_getStart")))
        get_started_link.click()
        login_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.investorai.crypto:id/btn_login")))

        # Enter username, password and tap Login button
        driver.find_element(AppiumBy.ID, "com.investorai.crypto:id/et_username").send_keys("xyz@bridgeweave.com");
        driver.find_element(AppiumBy.ID, "com.investorai.crypto:id/et_password").send_keys("xxxxxx")
        login_button.click()

        # Agree to terms and conditions
        agree_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.investorai.crypto:id/btn_agree")))
        agree_button.click()

        # wait for the chart to load
        wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.investorai.crypto:id/chart1")))
        wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.investorai.crypto:id/rb_allocationGraphCurrent")))

        # perform swipe up action to reach 'Add Strategy' button on the screen
        driver.swipe(start_x=520, start_y=1530, end_x=520, end_y=200, duration=1000)

        # click 'Add Strategy' button
        driver.find_element(AppiumBy.ID, "com.investorai.crypto:id/btn_addStrategy").click()
        alpha_hunter = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[2]/android.view.ViewGroup/android.widget.Button")))
        alpha_hunter.click()
        api_key = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.investorai.crypto:id/txt_account_name")))
        api_key.click()
        invest_amount = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.investorai.crypto:id/edit_investmentamount")))
        invest_amount.send_keys("500")
        driver.find_element(AppiumBy.ID, "com.investorai.crypto:id/btn_convert_moreUSD").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()