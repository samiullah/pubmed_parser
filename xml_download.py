from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# //driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get("https://www.ncbi.nlm.nih.gov/pubmed/")

# Enter your Search term here
search_term = "yoga" #enter search term in csv or yml file or xml file

#wait for download to get complete
#rename file to searchterm+timestamp
#create seperate file for downloads

assert "PubMed" in driver.title
search = driver.find_element_by_name("term")
search.clear()
search.send_keys(search_term)
search.send_keys(Keys.RETURN)

result = driver.find_element_by_xpath("//h3[@class='result_count left']")
result_string = result.text
final_result = result_string.split("of ")
print("Total Number of Results are: "+ final_result)

#Logic for handling usage of custom range based on number of results

result_count = int(result_string)

if result_count >9000:
    
else:
    pass

driver.execute_script("document.getElementsByClassName('tgt_dark')[3].click()")
driver.execute_script("document.getElementsByName('EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.SendTo')[0].click()")

driver.execute_script("document.getElementsByTagName('select')[2].value='xml'")
driver.execute_script("document.getElementsByName('EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.SendToSubmit')[0].click()")
# send_to.click()
# driver.close()

#pick the xml file from downloads

