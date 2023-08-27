import os
import boto3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def lambda_handler(event, context):
    try:
        
        options = Options()
        options.binary_location = '/opt/headless-chromium'
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--single-process')
        options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome('/opt/chromedriver', chrome_options=options)

        url = event['url'] 
        print("Opening URL:", url)
        driver.get(url)

        session_list = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'session-list'))
        )

        session_blocks = session_list.find_elements(By.CLASS_NAME, 'session-block')

        premium_seating_available = False 

        for session_block in session_blocks:
            title_seating = session_block.find_element(By.CLASS_NAME, 'title-seating').text
            if title_seating == 'Premium Seating':
                times_div = session_block.find_element(By.CLASS_NAME, 'times')
                time_elements = times_div.find_elements(By.CLASS_NAME, 'time')
                for time_element in time_elements:
                    if 'filling' in time_element.get_attribute('class'):
                        premium_seating_available = True
                        break

        sns_topic_arn = "arn:aws:sns:ap-southeast-2:832672331239:oppenheimer"
        sns_client = boto3.client('sns')

        if premium_seating_available:
            message = "Premium tickets now available! \n" + url + "\nHURRY UP!"
            sns_client.publish(TopicArn=sns_topic_arn, Message=message)

            # Raise an exception with the errorCode field
            raise Exception("Tickets are available. Stopping Step Function.")
        else:
            response = {
                "statusCode": 200,
                "body": "TicketsNotAvailable",
            }
            
        driver.quit()
        return response
    except Exception as e:
        error_response = {
            "statusCode": 500,
            "body": "An error occurred: " + str(e)
        }
        return error_response