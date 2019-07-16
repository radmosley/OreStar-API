start_date = [
    '01/01/2012', 
    '01/19/2012',
    '02/01/2012',
    '02/15/2012',
    '03/01/2012',
    '03/1/2012',
    '04/01/2012',
    '04/19/2012',
    '05/01/2012',
    '05/19/2012',
    '06/01/2012',
    '06/19/2012',
    '07/01/2012',
    '07/19/2012',
    '08/01/2012',
    '08/19/2012',
    '09/01/2012',
    '09/19/2012',
    '10/01/2012',
    '10/19/2012',
    '11/01/2012',
    '11/19/2012',
    '12/01/2012',
    '12/19/2012',
    '01/01/2013', 
    '01/19/2013',
    '02/01/2013',
    '02/15/2013',
    '03/01/2013',
    '03/19/2013',
    '04/01/2013',
    '04/19/2013',
    '05/01/2013',
    '05/19/2013',
    '06/01/2013',
    '06/19/2013',
    '07/01/2013',
    '07/19/2013',
    '08/01/2013',
    '08/19/2013',
    '09/01/2013',
    '09/19/2013',
    '10/01/2013',
    '10/19/2013',
    '11/01/2013',
    '11/19/2013',
    '12/01/2013',
    '12/19/2013',
    


]
end_date = [
    '01/18/2012', 
    '01/31/2012',
    '02/16/2012',
    '02/29/2012',
    '03/18/2012',
    '03/31/2012',
    '04/18/2012',
    '04/30/2012',
    '05/18/2012',
    '05/31/2012',
    '06/18/2012',
    '06/30/2012',
    '07/18/2012',
    '07/31/2012',
    '08/18/2012',
    '08/31/2012',
    '09/18/2012',
    '09/30/2012',
    '10/18/2012',
    '10/31/2012',
    '11/18/2012',
    '11/30/2012',
    '12/18/2012',
    '12/31/2012',
    '01/18/2013', 
    '01/31/2013',
    '02/16/2013',
    '02/28/2013',
    '03/18/2013',
    '03/31/2013',
    '04/18/2013',
    '04/30/2013',
    '05/18/2013',
    '05/31/2013',
    '06/18/2013',
    '06/30/2013',
    '07/18/2013',
    '07/31/2013',
    '08/18/2013',
    '08/31/2013',
    '09/18/2013',
    '09/30/2013',
    '10/18/2013',
    '10/31/2013',
    '11/18/2013',
    '11/30/2013',
    '12/18/2013',
    '12/31/2013',
    ]

for x in len(start_date)-1:
    #Grab form and button elements
    start = driver.find_element_by_id('cneSearchTranStartDate')
    end = driver.find_element_by_id('cneSearchTranEndDate')
    search_button = driver.find_element_by_name('search')

    #Clear form input by default and input start and end dates
    start.clear()
    start.send_keys(start_date[x])
    end.clear()
    end.send_keys(end_date[x])
        
    #click search button
    search_button.click()
    print('searching dates')
    print(start_date + ' ' + end_date)
    
    # try:
    #     wait = WebDriverWait(driver, 10)
    #     # download = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Excel Format"))).send_keys(Keys.COMMAND + 't') 
    #     download = driver.find_element_by_partial_link_text('Excel Format')
    #     #Download the excel file
    #     download.click()
    #     time.sleep(30)
    #     driver.quit()
    #     print("downloading file")

    # except TimeoutException:
    #     print("Loading took too much time!")