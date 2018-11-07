# IMPORTS:
import random
import time
import csv
from selenium import webdriver
from datetime import datetime

# CONFIGURATION:
table_path=('phantomjs')
driver = webdriver.Chrome(executable_path='chromedriver')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('headless')
# driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
driver.set_window_size(1124, 1200)

# DECLARATIONS:
topics = open('topics.txt', 'r')
set_of_words = topics.read().split('\n')
output_file = open('scores.csv', 'w')
writer = csv.writer(output_file)
log_file = open('log.txt', 'w')
topic_count = 0

# EVALUATION:
start_time = datetime.now()
log_file.write("Evaluation started at: " + str(start_time) + "\n")
for words in set_of_words[0:-1]:
    # Access the website:
    driver.get('http://palmetto.aksw.org/palmetto-webapp/')
    time.sleep(5)
    topic_count += 1 # Topic counter + 1.
    print("\nTOPIC: ", topic_count) # Print the current topic.
    log_file.write("\nTOPIC: " + str(topic_count) + "\n") # Write the current topic on log file.

    # Fill the field with the topic and click the submit button:
    words1 = driver.find_element_by_id("words")
    words1.send_keys(words)
    button = driver.find_element_by_id("submitButton")
    time.sleep(5)

    # CV Coherence:
    CV_start_time = datetime.now()
    buttonCv = driver.find_element_by_xpath('//*[@id="coherence_radio"]/label[1]/span/span')
    buttonCv.click()
    button.click()
    time.sleep(5)
    success = False
    CV_try = 0
    while not success:
        CV_try += 1
        time.sleep(1)
        try:
            cv=([driver.find_element_by_xpath('//*[@id="resultsTable"]/tbody/tr/td[3]').text])
            success = True
        except:
            pass
        print("  [CV] Coherence TRY: ", CV_try) # Print the current coherence try to get the score.
        log_file.write("  [CV] Coherence TRY: " + str(CV_try) + "\n") # Write the current coherence try to get the score into the log file.
    CV_end_time = datetime.now() - CV_start_time
    print("  =[CV] Time to Evaluate: " + str(CV_end_time))
    log_file.write("  =[CV] Time to Evaluate: " + str(CV_end_time) + "\n")
    print("  =[CV] Score: " + str(cv))
    log_file.write("  =[CV] Score: " + str(cv) + "\n")

    # CP Coherence:
    CP_start_time = datetime.now()
    buttonCp = driver.find_element_by_xpath('//*[@id="coherence_radio"]/label[2]/span/span')
    buttonCp.click()
    button.click()
    time.sleep(5)
    success = False
    CP_try = 0
    while not success:
        CP_try += 1
        time.sleep(1)
        try:
            cp=([driver.find_element_by_xpath('//*[@id="resultsTable"]/tbody/tr[2]/td[3]').text])
            success = True
        except:
            pass
        print("  [CP] Coherence TRY: ", CP_try) # Print the current coherence try to get the score.
        log_file.write("  [CP] Coherence TRY: " + str(CP_try) + "\n") # Write the current coherence try to get the score into the log file.
    CP_end_time = datetime.now() - CP_start_time
    print("  =[CP] Time to Evaluate: " + str(CP_end_time))
    log_file.write("  =[CP] Time to Evaluate: " + str(CP_end_time) + "\n")
    print("  =[CP] Score: " + str(cp))
    log_file.write("  =[CP] Score: " + str(cp) + "\n")

    # CUCI Coherence:
    CUCI_start_time = datetime.now()
    buttonCuci = driver.find_element_by_xpath('//*[@id="coherence_radio"]/label[3]/span/span')
    buttonCuci.click()
    button.click()
    time.sleep(5)
    success = False
    CUCI_try = 0
    while not success:
        CUCI_try += 1
        time.sleep(1)
        try:
            cuci=([driver.find_element_by_xpath('//*[@id="resultsTable"]/tbody/tr[3]/td[3]').text])
            success = True
        except:
            pass
        print("  [CUCI] Coherence TRY: ", CUCI_try) # Print the current coherence try to get the score.
        log_file.write("  [CUCI] Coherence TRY: " + str(CUCI_try) + "\n") # Write the current coherence try to get the score into the log file.
    CUCI_end_time = datetime.now() - CUCI_start_time
    print("  =[CUCI] Time to Evaluate: " + str(CUCI_end_time))
    log_file.write("  =[CUCI] Time to Evaluate: " + str(CUCI_end_time) + "\n")
    print("  =[CUCI] Score: " + str(cuci))
    log_file.write("  =[CUCI] Score: " + str(cuci) + "\n")

    # CUMASS Coherence:
    CUMASS_start_time = datetime.now()
    buttonCumass = driver.find_element_by_xpath('//*[@id="coherence_radio"]/label[4]/span/span')
    buttonCumass.click()
    button.click()
    time.sleep(5)
    success = False
    CUMASS_try = 0
    while not success:
        CUMASS_try += 1
        time.sleep(1)
        try:
            cumass=([driver.find_element_by_xpath('//*[@id="resultsTable"]/tbody/tr[4]/td[3]').text])
            success = True
        except:
            pass
        print("  [CUMASS] Coherence TRY: ", CUMASS_try) # Print the current coherence try to get the score.
        log_file.write("  [CUMASS] Coherence TRY: " + str(CUMASS_try) + "\n") # Write the current coherence try to get the score into the log file.
    CUMASS_end_time = datetime.now() - CUMASS_start_time
    print("  =[CUMASS] Time to Evaluate: " + str(CUMASS_end_time))
    log_file.write("  =[CUMASS] Time to Evaluate: " + str(CUMASS_end_time) + "\n")
    print("  =[CUMASS] Score: " + str(cumass))
    log_file.write("  =[CUMASS] Score: " + str(cumass) + "\n")

    # CNPMI Coherence:
    CNPMI_start_time = datetime.now()
    buttonCnpmi = driver.find_element_by_xpath('//*[@id="coherence_radio"]/label[5]/span/span')
    buttonCnpmi.click()
    button.click()
    time.sleep(5)
    success = False
    CNPMI_try = 0
    while not success:
        CNPMI_try += 1
        time.sleep(1)
        try:
            cnpmi=([driver.find_element_by_xpath('//*[@id="resultsTable"]/tbody/tr[5]/td[3]').text])
            success = True
        except:
            pass
        print("  [CNPMI] Coherence TRY: ", CNPMI_try) # Print the current coherence try to get the score.
        log_file.write("  [CNPMI] Coherence TRY: " + str(CNPMI_try) + "\n") # Write the current coherence try to get the score into the log file.
    CNPMI_end_time = datetime.now() - CNPMI_start_time
    print("  =[CNPMI] Time to Evaluate: " + str(CNPMI_end_time))
    log_file.write("  =[CNPMI] Time to Evaluate: " + str(CNPMI_end_time) + "\n")
    print("  =[CNPMI] Score: " + str(cnpmi))
    log_file.write("  =[CNPMI] Score: " + str(cnpmi) + "\n")

    # CA Coherence:
    CA_start_time = datetime.now()
    buttonCa = driver.find_element_by_xpath('//*[@id="coherence_radio"]/label[6]/span/span')
    buttonCa.click()
    button.click()
    time.sleep(5)
    success = False
    CA_try = 0
    while not success:
        CA_try += 1
        time.sleep(1)
        try:
            ca=([driver.find_element_by_xpath('//*[@id="resultsTable"]/tbody/tr[6]/td[3]').text])
            success = True
        except:
            pass
        print("  [CA] Coherence TRY: ", CA_try) # Print the current coherence try to get the score.
        log_file.write("  [CA] Coherence TRY: " + str(CA_try) + "\n") # Write the current coherence try to get the score into the log file.
    CA_end_time = datetime.now() - CA_start_time
    print("  =[CA] Time to Evaluate: " + str(CA_end_time))
    log_file.write("  =[CA] Time to Evaluate: " + str(CA_end_time) + "\n")
    print("  =[CA] Score: " + str(ca))
    log_file.write("  =[CA] Score: " + str(ca) + "\n")

    # Write all topic scores:
    writer.writerow([words,cv,cp,cuci,cumass,cnpmi,ca])
    time.sleep(5)

end_time = datetime.now() - start_time
print("\nALL TOPICS SUCCESSFUL EVALUATED!")
log_file.write("\nALL TOPICS SUCCESSFUL EVALUATED!")
print("Time to Evaluate: " + str(end_time))
log_file.write("Time to Evaluate: " + str(end_time))
