#! /usr/bin/env python3

import os
import requests

path = "data/feedback/"
ip = "34.72.214.255"

def get_txt(path):
    dirs=[]
    for dir in os.listdir(path):
        if "txt" in dir:
            dirs.append(dir)
    return dirs

def txt_to_feedback(file):
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]

        feedback={}
        feedback["title"] = lines[0]
        feedback["name"] = lines[1]
        feedback["date"] = lines[2]
        feedback["feedback"] = lines[3]
    return feedback

def post_feedback(json):
    response = requests.post(f"http:/{ip}/feedback/", data=json)
    print(response.status_code)

def main():
    dirs = get_txt(path)
    for dir in dirs:
        file = path + "/" + dir
        feedback = txt_to_feedback(file)
        post_feedback(feedback)

if __name__ == '__main__':
    main()