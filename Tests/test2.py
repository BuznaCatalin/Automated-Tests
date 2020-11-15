from selenium import webdriver


def test_card_is_displayed():
    driver = webdriver.Chrome(executable_path=r'C:\Chromedriver\chromedriver.exe')
    # maximize windows
    driver.set_window_size(1024, 600)
    driver.maximize_window()

    # 1. Go to statsroyale
    driver.get('https://statsroyale.com/')

    # 2. Accept cookies
    driver.find_element_by_xpath("//span[contains(@id,'cmpbntyestxt')]").click()

    # 3. Assert Golem is displayed
    #driver.find_element_by_xpath("//a[@href='/cards']").click()
    driver.find_element_by_css_selector("[href='/cards']").click()
    card_golem = driver.find_element_by_css_selector("[src*='chr_golem']")
    assert card_golem.is_displayed()


def test_is_legendary():
    driver = webdriver.Chrome(executable_path=r'C:\Chromedriver\chromedriver.exe')
    # maximize windows
    driver.set_window_size(1024, 600)
    driver.maximize_window()

    # 1. Go to statsroyale
    driver.get('https://statsroyale.com/')

    # 2. Accept cookies
    driver.find_element_by_xpath("//span[contains(@id,'cmpbntyestxt')]").click()

    # 3. Go to cards page
    driver.find_element_by_xpath("//a[@href='/cards']").click()

    # 4. Click on legendary card to diselect
    driver.find_element_by_id('legendary-cards').click()

    # 5. Assert if Hound is not displayed
    hound_card = driver.find_element_by_css_selector("[src*='lava_hound']")
    assert hound_card.is_displayed() == False



