Hi Elementor,
I was started investigating and quering the response payload in order to understand it's structure and data, and suddenly i started recieving an errors.
I got an email from virustotal that i was ran out of API quota and couldn't advance with the solution.

ATTENTION: You have consumed your VirusTotal API quota
Hello,
This is a notification to let you know that you have exceeded the following VirusTotal API allowances:
- Daily API quota
So all your lookups needing those privileges are now getting status code 429 Quota Exceeded responses. As a consequence your scripts may start to fail.

At VirusTotal we are always willing to work together to gather as many files and malware information as possible in order to improve the global understanding of threats, please do not hesitate to contact us via https://www.virustotal.com/gui/contact-us in order to discover how you can get more quota.

You may rather want to get started straight away with a Premium API trial, discover what VirusTotal can do for your organization at: https://www.virustotal.com/gui/services-overview

Kind regards.

Installation
run pip install -r requirements.txt

Suggestions for improvements or changes
1. create it as flask web app api as a microservice architecture (config, route, model, service etc).
2. if i had to build it as a simple etl app:
3. in each url iteration load the response into a list of responses and at the end load the list of responses into a pandas dataframe.
4. use get/defaultdict on json quering to avoid keys error.
5. load the responses dataframe into a data\rawdata.csv file for better investigation. 
6. add 2 new fields using "df.assign" method to the main dataframe acording to the requirements logic -> risk\safe datasite & total voting.
7. load the dataframe to db using sqlalchemy(to_sql).
8. add exception handling (try,except,finally).
9. add logger.
