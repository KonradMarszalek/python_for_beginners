from selenium import webdriver

driver = webdriver.Chrome('/Users/kmarszalek/code/python_for_beginners/airhelp/chromedriver')
driver.get("https://www.airhelp.com/en/")
assert "Get Compensation for Flight Delays of up to $700 | AirHelp" in driver.title

start_airport = "Rebiechowo Airport, GDN"
flight_destination = "J. Paul II International Airport Krakow-Balice, KRK"

elem = driver.find_element_by_id("start-airport")
elem.send_keys(start_airport)
elem = driver.find_element_by_id("flight-destination")
elem.send_keys(flight_destination)
elem = driver.find_element_by_id("check-compensation-button")
elem.click()

elem = driver.find_element_by_xpath('//h3')
assert "Where did you fly?" in elem.text

driver.close()
