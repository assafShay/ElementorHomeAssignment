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
1. create it as flask web app api with a microservice architecture (config, route, model, service etc).
2. if i had to build it as a simple etl app:
3. in each url iteration load the response into a list of responses and at the end load the list of responses into a pandas dataframe.
4. use get/defaultdict on json quering to avoid keys error.
5. load the responses dataframe into a data\rawdata.csv file for better investigation. 
6. add 2 new fields using "df.assign" method to the main dataframe acording to the requirements logic -> risk\safe datasite & total voting.
7. load the dataframe to db using sqlalchemy(to_sql).
8. add exception handling (try,except,finally).
9. add logger.

after getting another amount of available requests today, the run function should look like this:
ofcourse i need to implement a db insert of the df using sqlalchemy to_sql method.

def run():
    with open('data\\request1.csv', newline='') as read_obj:
        csv_reader = csv.reader(read_obj)
        list_of_urls = list(csv_reader)

        response_list = []
        for url in list_of_urls:
            url_id = base64.urlsafe_b64encode(url[0].encode()).decode().strip("=")
            response = get_url_analysis_report(url_id)
            response_list.append(response["data"]["attributes"])

        df = pd.DataFrame.from_dict(response_list)
        df.to_csv('data\\raw_data.csv', index=False)

        analysis_list = df['last_analysis_results'].tolist()

        result_list = []
        for analysis in analysis_list:
            analysis_results_list = []
            for k, v in analysis.items():
                analysis_results_list.append(v["result"])
            result = dict(Counter(analysis_results_list))
            result_list.append(result)

        df = df.assign(analysis_results=result_list)
        df.to_csv('data\\analysis_results.csv', index=False)
        
        site_risk_list = []
        for result in result_list:
            if ("malicious" in result or "phishing" in result_list or "malware" in result_list):
                site_risk_list.append("risk")
            else:
                site_risk_list.append("safe")

        df = df.assign(site_risk=site_risk_list)
        df.to_csv('data\\site_risk.csv', index=False)
