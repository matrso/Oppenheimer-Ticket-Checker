# Oppenheimer Ticket Checker

## Project Overview

### Imax Ticket Notifier for Oppenheimer Movie

The Imax Ticket Notifier for the Oppenheimer movie is a serverless Python-based project designed to help users secure premium seating tickets for the highly anticipated Oppenheimer screenings at Melbourne's Imax theater. Leveraging the power of AWS services and Selenium for web scraping, this project employs a serverless architecture to continuously monitor the Imax website for the availability of premium seating tickets. Upon detection of newly available tickets, the user receives an SMS or email notification, enabling swift reservation of the best seats for the movie.

## Solution Overview
The Imax Ticket Notifier embraces a serverless architecture, harnessing the capabilities of various AWS services to achieve its objective:

**• Architecture:** The project is built on a serverless approach, utilizing AWS Lambda, Step Functions, EventBridge, and CloudWatch for efficient execution.

**• AWS Lambda and Dependencies Layer:** The core Python script, integrated with Selenium and a headless Chromium browser, resides within a Lambda function. This function's dependencies, housed in a Lambda layer, are conveniently accessible via an S3 bucket.

**• AWS Step Functions and EventBridge:** Step Functions coordinate the workflow, with EventBridge acting as the scheduling trigger. EventBridge invokes the Step Function at regular intervals, initiating the ticket availability monitoring process.

**• Amazon SNS Notification:** Upon detecting new premium seating tickets, the Lambda function triggers a positive notification message through an Amazon SNS topic. This topic is configured to deliver notifications via SMS or email, tailored to user preferences.

## How It Works
The Imax Ticket Notifier operates as follows:

The Python script, powered by Selenium and a headless Chromium browser, systematically searches Melbourne's Imax website for premium seating tickets to Oppenheimer sessions.

• AWS Lambda executes the script, employing the Selenium-powered browser to identify the availability of premium seating tickets.

• Upon confirming available tickets, the Lambda function triggers a positive notification message through an Amazon SNS topic.
The SNS topic promptly delivers notifications to users, enabling them to promptly secure the best seats for the movie.

• AWS Step Functions manage the workflow, while EventBridge schedules recurring Lambda function invocations.

• The Lambda function concludes its execution upon successfully finding premium seating tickets, ensuring resource efficiency, preventing unnecessary invocations, and avoiding spamming users.

• Comprehensive logs documenting the behavior of each component are stored in AWS CloudWatch, facilitating effective system monitoring and troubleshooting.


By leveraging the power of AWS services, focusing on premium seating tickets, utilizing Selenium for web scraping, and automatically halting Lambda execution upon success, the Imax Ticket Notifier offers an efficient and reliable solution for securing premium seats for the Oppenheimer movie.
