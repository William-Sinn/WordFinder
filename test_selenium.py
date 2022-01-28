from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://youtube.com')

searchbar = driver.find_element_by_xpath(
    '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
searchbar.send_keys('red hot knife')

searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()

# list1 = ['a', 'b', 'c', 4, 213, 567]
# list2 = ['a', 'c', 567]
# list3 =[]
# for item in list1:
#     if item not in list2:
#         list3.append(item)
# print(list3)
