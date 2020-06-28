'''
This script will parse and validate the current known issues includes from Azure Stack Hub
(6/27/2020).
'''

import os
import cerberus
import csv
import json

import val_ki_functions as VAL

KNOWNISSUES = r"C:\git\mb\azs-modular-poc\docfx_project\includes"
KNOWNISSUESTABLE = "C:\\git\\mb\\azs-modular-poc\\python\\data\\knownissues_validation.csv"
SCHEMA = r"C:\git\mb\azs-modular-poc\python\data\schema_include_beta.json"


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


def main():
    '''Validate includes in the repo.'''
    include_paths = get_files(KNOWNISSUES)
    with open(SCHEMA) as fh:
        schema_include = json.load(fh)
    report = []
    report.append(["issueid", "validation status"])
    for p in include_paths:
        if p.find("issue_azs") > -1:
            inbody = get_textfromMD(p)
            try:
                if VAL.validate_base_file(inbody):
                    include_head = "###"
                    tokens = ["Applicable", "Cause", "Remediation", "Occurrence"]
                    include_body = VAL.parse_include(inbody, include_head, tokens)
                    print(VAL.validate_summary(schema_include, include_body))
                else:
                    print(" {'summary': False, 'details' : {'error' : 'Not a valid include file: " + p.split("\\")[-1] + "}")
            except Exception as e:
                    print(" {'summary': False, 'details' : {'error' : 'Not a valid include file: " + p.split("\\")[-1] + " " + str(e) + "}")


if __name__ == "__main__":
    main()
