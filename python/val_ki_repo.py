'''
This script will parse and validate the current known issues includes from Azure Stack Hub
(6/27/2020).

    The function runs validates the includes in the repository.

    1.  Configure the script by updating the global variables.
        MODULES points to the module folder.
        SCHEMA points to the module schema rule set.
        VALIDATIONREPORT points to the location of the validation report.

        Note: currently keyed to only find known issues by filtering by the key in 
        the file name 'issue_azs'

    2.  Run the script.
    3.  Open the validation report.

'''

import os
import csv
import json

import val_ki_functions as VAL
import mod_utilities as MU

MODULES = r"C:\git\mb\azs-modular-poc\docfx_project\includes"
SCHEMA = r"C:\git\mb\azs-modular-poc\python\schemas\known_issue.json"
VALIDATIONREPORT = "C:\\git\\mb\\azs-modular-poc\\python\\data\\knownissues_report_validation.csv"


def repo_logic(indict):
    '''Insert the logic to process the return from the function.'''
    print(indict)

def main():
    '''
        Validate includes in the repo. (Main Logic for repo parsing)
    '''
    include_paths = MU.get_files(MODULES)
    report = []
    report.append(["issueid", "validation status", "path", "error"])
    for p in include_paths:
        if p.find("known-issue") > -1:
            inbody = MU.get_textfromMD(p)
            valid_id = p.split("\\")[-1][:-3]
            print("Validating " + valid_id[6:])
            try:
                if VAL.validate_base_file(inbody):
                    body_parse = VAL.parse_module(inbody)
                    v_line = VAL.validate_module_ki(SCHEMA, body_parse)
                    if v_line["summary"]:
                        report.append([valid_id, v_line["summary"], p, "No error."])
                    else:
                        fields = list(v_line["details"].keys())
                        for f in fields:
                            error_message = "{}: {}".format(v_line["details"][f][0], f)
                            report.append([valid_id, v_line["summary"], p, error_message ])
                else:
                    report.append([valid_id, False, p, "Not a valid include file."])
            except Exception as e:
                    report.append([valid_id, False, p, "Not a valid include file. {}".format(e)])
    MU.write_csv(report, VALIDATIONREPORT)
    print("The validation report saved to: " + VALIDATIONREPORT)

if __name__ == "__main__":
    main()
