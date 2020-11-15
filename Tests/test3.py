from selenium import webdriver


def test_singleInputField():
    driver = webdriver.Chrome(executable_path=r'C:\Chromedriver\chromedriver.exe')
    pageUrl = "http://www.seleniumeasy.com/test/basic-first-form-demo.html"
    driver.maximize_window()
    driver.get(pageUrl)

    # Finding "Single input form" input text field by id. And sending keys(entering data) in it
    eleUserMessage = driver.find_element_by_id("user-message")
    eleUserMessage.clear()
    eleUserMessage.send_keys("Test Python")

    # Finding "Show Your Message" button element by css selector using both id and class name. And clicking it.
    btn1 = driver.find_element_by_xpath("//button[contains(text(),'Show Message')]")
    btn1.click()

    # Checking whether the input text and output text are same using assertion.
    eleYourMsg = driver.find_element_by_id("display")
    assert "Test Python" in eleYourMsg.text

def test_twoInputField():
    driver = webdriver.Chrome(executable_path=r'C:\Chromedriver\chromedriver.exe')
    pageUrl = "http://www.seleniumeasy.com/test/basic-first-form-demo.html"
    driver.maximize_window()
    driver.get(pageUrl)

    # Finding "Two input form" input text field by id. And sending keys(entering data) in it.
    a = driver.find_element_by_id('sum1')
    a.clear()
    a.send_keys('5')

    b =driver.find_element_by_id('sum2')
    b.clear()
    b.send_keys('5')

    btn2 = driver.find_element_by_xpath("//button[contains(text(),'Get Total')]")
    btn2.click()

    msg = driver.find_element_by_id('displayvalue')
    assert '10' in msg.text


