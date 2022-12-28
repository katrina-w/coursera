#!/usr/bin/env python3

import os
from datetime import datetime
import sys
import reports
import emails


def write_content(path):
    report_content = ""
    for dir in os.listdir(path):
        if "txt" in dir: 
            with open(path + "/" + dir) as f:
                lines = [line.rstrip('\n') for line in f]
                
                report_content += "name: {}".format(lines[0])
                report_content += "<br />"
                report_content += "weight: {}".format(lines[1])
                report_content += "<br />"
    return report_content

def write_title():
    str_tdy = datetime.today().strftime('%Y-%m-%d')
    title = "Processed Update on {}".format(str_tdy)
    return title

def main(argv):
    path = "supplier-data/descriptions/"
    report_title = write_title()
    report_content = write_content(path)
    reports.generate_report("/tmp/processed.pdf", report_title, report_content)

    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)


if __name__ == "__main__":
    main(sys.argv)