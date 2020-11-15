from selenium import webdriver

def test_google_search():
    driver = webdriver.Chrome(executable_path=r'C:\Chromedriver\chromedriver.exe')
    driver.get('https://google.com')

    driver.find_element_by_name('q').send_keys('selenium')

    driver.find_element_by_name('btnK').submit()

    assert 'selenium' in driver.title

