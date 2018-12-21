from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import date
import time


#Logic for handling usage of custom range based on number of results
# use recursive method divide range until  u get <9000
# rename csv file for total custom range


item_to_search = "cancer"
From_date = "2010-12-01"
to_date = "2018-12-01"

no_of_days = 100 

def download_xml_file():
    driver = webdriver.Chrome()
    driver.execute_script("document.getElementsByClassName('tgt_dark')[3].click()")
    driver.execute_script("document.getElementsByName('EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.SendTo')[0].click()")
    driver.execute_script("document.getElementsByTagName('select')[2].value='xml'")
    driver.execute_script("document.getElementsByName('EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.SendToSubmit')[0].click()")
    send_to.click()
    driver.close()

# #This function will return number of records for an item in given date range

def Input_given_date_range_to_get_records_count(item_to_search):
    driver = webdriver.Chrome()
    driver.get("https://www.ncbi.nlm.nih.gov/pubmed/")
    assert "PubMed" in driver.title
    
    search = driver.find_element_by_name("term")
    search.clear()
    search.send_keys(item_to_search)
    search.send_keys(Keys.RETURN)
    custom_range = driver.find_element_by_xpath("//a[@href='#facet_date_range_divds1']")
    custom_range.click()

    from_year = driver.find_element_by_xpath("//input[@id='facet_date_st_yeards1']")
    from_year.clear()
    from_year.send_keys("")
    time.sleep(5)
    from_year.send_keys("2010")
    time.sleep(5)
    # from_year.send_keys(Keys.TAB)

    from_month = driver.find_element_by_xpath("//input[@id='facet_date_st_monthds1']")
    from_month.send_keys("")
    time.sleep(5)
    from_month.clear()
    time.sleep(3)
    from_month.send_keys("12")
    time.sleep(5)

    from_day = driver.find_element_by_xpath("//input[@id='facet_date_st_dayds1']")
    from_day.send_keys("")
    time.sleep(5)
    from_day.clear()
    from_day.send_keys("02")
    time.sleep(5)


    To_year = driver.find_element_by_xpath("//input[@id='facet_date_end_yeards1']")
    To_year.clear()
    To_year.send_keys("")
    time.sleep(5)
    To_year.send_keys("2018")
    time.sleep(5)
    # To_year.send_keys(Keys.TAB)

    To_month = driver.find_element_by_xpath("//input[@id='facet_date_end_monthds1']")
    To_month.send_keys("")
    time.sleep(5)
    To_month.clear()
    time.sleep(3)
    To_month.send_keys("12")
    time.sleep(5)

    To_day = driver.find_element_by_xpath("//input[@id='facet_date_end_dayds1']")
    To_day.send_keys("")
    time.sleep(5)
    To_day.clear()
    To_day.send_keys("02")
    time.sleep(5)

    apply_button = driver.find_element_by_xpath("//button[@id='facet_date_range_applyds1']")

    apply_button.click()

    time.sleep(5)

    

    result = driver.find_element_by_xpath("//h3[@class='result_count left']")
    result_string = result.text
    No_of_records = result_string.split("of ")
    No_of_records = No_of_records[1]
    No_of_records = int(No_of_records)
    print(type(No_of_records))
    print(No_of_records)
    return No_of_records
    

x = Input_given_date_range_to_get_records_count(item_to_search)


# # This function Will return a dictionary for date range
def Get_custom_year_range():
    date_range = {}
    number_of_records = x 
    if number_of_records <= 9000:
        date_range[1]=(From_date, to_date)
        return date_range
    else:
        iPossible_date_range_count = number_of_records/9000
        iPossible_date_range_count = round(iPossible_date_range_count)
        print("*******iPossible_date_range_count******")
        print(iPossible_date_range_count)
        print('***************************************')
        from datetime import datetime,timedelta
        date_format = "%Y-%m-%d"
        a = datetime.strptime(to_date, date_format)
        b = datetime.strptime(From_date, date_format)
        delta = a-b
        no_of_days = delta.days
        print("no_of_days")
        print(no_of_days)
        print('***************************************')
        days_per_period = no_of_days/iPossible_date_range_count
        days_per_period = round(days_per_period)
        print("days_per_period")
        print(days_per_period)
        from datetime import datetime
        from datetime import timedelta
        date_format = "%Y-%m-%d"
        fromdate= datetime.strptime(From_date, date_format)
        todate = datetime.strptime(to_date, date_format)
        for i in range(iPossible_date_range_count):
            date_range[i]=(fromdate,fromdate+timedelta(days_per_period))
            fromdate = fromdate+timedelta(days_per_period)+timedelta(1)
        return date_range

print(Get_custom_year_range())


# reverse 
# date range correctly
# complete csv -- rename  todaysdate+fromdate+searchterm.csv 19122018_01012006_yoga put in folder yoga 