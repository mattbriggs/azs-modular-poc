'''
This script will parse the current known issues includes from Azure Stack Hub.
And produce a report.
(7/22/2020).
'''

import os
import csv
import json

import val_ki_functions as VAL

KNOWNISSUES = r"C:\git\mb\azs-modular-poc\docfx_project\includes"
KNOWNISSUESTABLE = "C:\\git\\mb\\azs-modular-poc\\python\\data\\knownissues_validation.csv"
SCHEMA = r"C:\git\mb\azs-modular-poc\python\data\schema_include_beta.json"
KNOWNISSUESREPORT = "C:\\git\\mb\\azs-modular-poc\\python\\data\\knownissues_report_powerbi.csv"

KNOWN_ISSUES_SCHEMA = ["ms.issue-id", 
                    "author", 
                    "ms.service",
                    "ms.topic",
                    "ms.date",
                    "ms.author",
                    "ms.reviewer",
                    "ms.lastreviewed",
                    "ms.sub-service",
                    "applicable",
                    "cause",
                    "remediation",
                    "occurrence"]


def get_textfromMD(path):
    '''Return text from a MD filename path'''
    textout = ""
    fh = open(path, "r")
    for line in fh:
        textout += line
    fh.close()
    return textout


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


def main():
        '''Parse the known issue includes in the repo.'''
        print("Starting")
        include_paths = get_files(KNOWNISSUES)
        report = []
        report.append(KNOWN_ISSUES_SCHEMA)
        for p in include_paths:
            if p.find("issue_azs") > -1:
                inbody = get_textfromMD(p)
                valid_id = p.split("\\")[-1][:-3][6:]
                print("parsing ... {}".format(valid_id))
                try:
                    include_head = "###"
                    tokens = ["Applicable", "Cause", "Remediation", "Occurrence"]
                    include_body = VAL.parse_include(inbody, include_head, tokens)
                    record = [include_body["ms.issue-id"],
                                include_body["author"],
                                include_body["ms.service"],
                                include_body["ms.topic"],
                                include_body["ms.date"],
                                include_body["ms.author"],
                                include_body["ms.reviewer"],
                                include_body["ms.lastreviewed"],
                                include_body["ms.sub-service"],
                                include_body["Applicable"],
                                include_body["Cause"],
                                include_body["Remediation"],
                                include_body["Occurrence"]]
                    report.append(record)
                except Exception as e:
                    record = [valid_id, "", "", "", "", "", "", "", "", "", "Validation error.", e, ""]
                    report.append(record)
        write_csv(report, KNOWNISSUESREPORT)
        print("End")


if __name__ == "__main__":
    main()


    ["ms.issue-id", 
                    "author", 
                    "ms.service",
                    "ms.topic",
                    "ms.date",
                    "ms.author"
                    "ms.reviewer",
                    "ms.lastreviewed",
                    "ms.sub-service",
                    "applicable",
                    "cause",
                    "remediation",
                    "occurrence"]