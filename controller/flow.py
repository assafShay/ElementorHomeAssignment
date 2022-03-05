"""flow"""
import csv
import base64
from controller.extract import *
from collections import Counter


def run():
    with open('data\\request1.csv', newline='') as read_obj:
        csv_reader = csv.reader(read_obj)
        list_of_urls = list(csv_reader)

        for url in list_of_urls:
            url_id = base64.urlsafe_b64encode(url[0].encode()).decode().strip("=")
            response = get_url_analysis_report(url_id)
            
            result_list = []
            for k, v in response["data"]["attributes"]["last_analysis_results"].items():
                result_list.append(v["result"])

            result_dict = Counter(result_list)
            result_dict["url"] = url

            print(dict(result_dict))

            if "malicious" in result_list:
                if "phishing" in result_list:
                    if "malware" in result_list:
                        print(f"{url}: risk")
            else:
                print(f"{url}: safe")
