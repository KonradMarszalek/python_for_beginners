from selenium import webdriver

chrome = webdriver.Chrome("/Users/kmarszalek/code/python_for_beginners/airhelp/chromedriver")

chrome.get("https://www.airhelp.com/en/")

assert 'Get Compensation for Flight Delays of up to' in chrome.title
assert "AirHelp" in chrome.title

element = chrome.find_element_by_id("start-airport")
element.send_keys("GDN")

chrome.find_element_by_id("flight-destination").send_keys("KRK")
chrome.find_element_by_id("check-compensation-button").click()

elements = chrome.find_elements_by_xpath("//h3")

# TODO: Fix it so it iterates through each element in elements
texts = []
for element in elements:
    texts.append(element.text)
assert "Where did you fly?" in texts
assert "Did you have any connecting flights?" in texts

chrome.close()
