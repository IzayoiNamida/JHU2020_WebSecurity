from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

url = "http://127.0.0.1/sampletest.html"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

total = 10
passed = 0

def test(a,b,c):
    global passed
    driver.find_element_by_id("a").clear()
    driver.find_element_by_id("a").send_keys(a)
    driver.find_element_by_id("b").clear()
    driver.find_element_by_id("b").send_keys(b)
    driver.find_element_by_id("bt").click()
    val = driver.find_element_by_id("c").text
    if int(val) == int(c):
        passed = passed + 1


if __name__ == "__main__":
    test(1,2,3)
    test(3,4,7)
    test(6,7,13)
    test(10,20,30)
    print(passed/total)