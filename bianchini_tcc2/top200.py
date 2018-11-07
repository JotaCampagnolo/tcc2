import random
import time
import csv
from selenium import webdriver

#table_path=('./phantomjs')
#driver = webdriver.Chrome(executable_path='./chromedriver')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('headless')
driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
topics = open('c200.txt', 'r')
#driver.set_window_size(1124, 850)

set_of_words = topics.read().split('\n')

output_file = open('re200.csv', 'a')
writer = csv.writer(output_file)
c=0

for words in set_of_words:
    driver.get('http://palmetto.aksw.org/palmetto-webapp/')
    time.sleep(1)
    c+=1
    print("TOPICO: ",c, end="\r")

    words1 = driver.find_element_by_id("words")
    words1.send_keys(words)
    button = driver.find_element_by_id("submitButton")
    button.click()
    time.sleep(120)

    try:
        cp=([driver.find_element_by_xpath('//*[@id="resultsTable"]/tbody/tr/td[3]').text])
    except:
        time.sleep(120)
        cp=([driver.find_element_by_xpath('//*[@id="resultsTable"]/tbody/tr/td[3]').text])
        continue

    buttonCv = driver.find_element_by_xpath('//*[@id="coherence_radio"]/label[2]/span/span')
    buttonCv.click()
    button.click()
    time.sleep(120)

    try:
        cv=([driver.find_element_by_xpath('//*[@id="resultsTable"]/tbody/tr[2]/td[3]').text])
    except:
        time.sleep(120)
        cv=([driver.find_element_by_xpath('//*[@id="resultsTable"]/tbody/tr[2]/td[3]').text])
        continue

    buttonCuci = driver.find_element_by_xpath('//*[@id="coherence_radio"]/label[3]/span/span')
    buttonCuci.click()
    button.click()
    time.sleep(120)

    try:
        cuci=([driver.find_element_by_xpath('//*[@id="resultsTable"]/tbody/tr[3]/td[3]').text])
    except:
        time.sleep(120)
        cuci=([driver.find_element_by_xpath('//*[@id="resultsTable"]/tbody/tr[3]/td[3]').text])
        continue

    buttonCumass = driver.find_element_by_xpath('//*[@id="coherence_radio"]/label[4]/span/span')
    buttonCumass.click()
    button.click()
    time.sleep(120)

    try:
        cumass=([driver.find_element_by_xpath('//*[@id="resultsTable"]/tbody/tr[4]/td[3]').text])
    except:
        time.sleep(120)
        cumass=([driver.find_element_by_xpath('//*[@id="resultsTable"]/tbody/tr[4]/td[3]').text])
        continue

    buttonCnpmi = driver.find_element_by_xpath('//*[@id="coherence_radio"]/label[5]/span/span')
    buttonCnpmi.click()
    button.click()
    time.sleep(120)

    try:
        cnpmi=([driver.find_element_by_xpath('//*[@id="resultsTable"]/tbody/tr[5]/td[3]').text])
    except:
        time.sleep(120)
        cnpmi=([driver.find_element_by_xpath('//*[@id="resultsTable"]/tbody/tr[5]/td[3]').text])
        continue

    buttonCa = driver.find_element_by_xpath('//*[@id="coherence_radio"]/label[6]/span/span')
    buttonCa.click()
    button.click()
    time.sleep(120)

    try:
        ca=([driver.find_element_by_xpath('//*[@id="resultsTable"]/tbody/tr[6]/td[3]').text])
    except:
        time.sleep(120)
        ca=([driver.find_element_by_xpath('//*[@id="resultsTable"]/tbody/tr[6]/td[3]').text])
        continue

    writer.writerow([cv,cp,cuci,cumass,cnpmi,ca])

    time.sleep(1)
print("TOPICO: 200")
