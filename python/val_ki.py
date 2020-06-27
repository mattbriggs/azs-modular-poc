'''
This script will parse and validate the current known issues includes from Azure Stack Hub
(6/27/2020).
'''

import os
import cerberus
import csv

import val_ki_dev as VAL

KNOWNISSUES = r"C:\git\mb\azs-modular-poc\docfx_project\includes"
KNOWNISSUESTABLE = "C:\\git\\mb\\azs-modular-poc\\python\\data\\knownissues_validation.csv"


def get_textfromMD(path):
    '''Return text from a MD filename path'''
    textout = ""
    fh = open(path, "r")
    for line in fh:
        textout += line
    fh.close()
    return textout


def write_csv(outbody, path):
    '''Write CSV file to the path.'''
    csvout = open(path, 'w', newline="")
    csvwrite = csv.writer(csvout)
    for r in outbody:
        try:
            csvwrite.writerow(r)
        except Exception as e:
            print("An error: {}".format(e))
    csvout.close()


def get_files(inpath):
    '''With the directory path, returns a list of markdown file paths.'''
    outlist = []
    for (path, dirs, files) in os.walk(inpath):
        for filename in files:
            ext_index = filename.find(".")
            if filename[ext_index+1:] == "md":
                entry = path + "\\" + filename
                outlist.append(entry)
    return outlist

def parse_known_issues(inbody):
    include = {}
    include["parse_state"] = "no"
    parts = inbody.split("---")
    body = parts[3].replace("\n### ", "^~")
    body = body.replace(":", "^~")

def main():
    '''Validate includes in the repo.'''
    include_paths = get_files(KNOWNISSUES)
    report = []
    report.append(["issueid", "validation status"])
    for p in include_paths:
        if p.find("issue_azs") > -1:
            inbody = get_textfromMD(p)
            include_head = "###"
            schemax = {'name': {'type': 'string'}}
            tokens = ["Applicable", "Cause", "Remediation", "Occurrence"]
            include_body = VAL.parse_include(inbody, include_head, tokens)
            print(VAL.validate_summary(include_body, schemax))


if __name__ == "__main__":
    main()
