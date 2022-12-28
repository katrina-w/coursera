# THIS PART IS UNTESTED. 
# I DID NOT SUBMIT THIS PART IN QWIKLABS FOR MY ASSIGNMENT.

#!/usr/bin/env python3

import psutil
import shutil
import socket
import sys
import emails
import os

def health_check():
    CPU_percent = psutil.cpu_percent()
    disk_usage = psutil.disk_usage('/').percent
    avail_mem = psutil.virtual_memory().available/ 1024 ** 2 
    local_host = socket.gethostbyname('localhost')

    conditions=[0,0,0,0]

    if CPU_percent > 80: conditions[0] = "Error - CPU usage is over 80%"
    if disk_usage < 0.2: conditions[1] = "Error - Available disk space is less than 20%"
    if avail_mem < 500: conditions[2] = "Error - Available memory is less than 500MB"
    if local_host != "127.0.0.1": conditions[3] = "Error - localhost cannot be resolved to 127.0.0.1"

    return conditions

def send_email(conditions):
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = " & ".join(str(condition) for condition in conditions if condition != 0)
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)


def main(argv):
    conditions = health_check()
    if conditions != [0,0,0,0]:
        send_email(conditions)

if __name__ == "__main__":
    main(sys.argv)