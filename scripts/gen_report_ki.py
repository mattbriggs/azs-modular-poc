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
SLUG = "known-issue"
POWERBIREPORT = "C:\\git\\mb\\azs-modular-poc\\data\\reports\knownissues_report_powerbi.csv"


def get_vals_as_list(cols, indict):
    '''Wtith a set of keys return the values in the order of the keys.'''
    row = []
    for col in cols:
        row.append(indict[col])
    return row


def main():
    ''' Parse the include modules and create a report.'''
    include_paths = MU.get_files(MODULES, "md")
    report = []
    headers = []
    for p in include_paths:
        if p.find(SLUG) > -1:
            inbody = MU.get_textfromMD(p)
            valid_id = p.split("\\")[-1][:-3]
            print("Reporting on " + valid_id[6:])
            try:
                if VAL.validate_base_file(inbody):
                    parsed_body = VAL.parse_module(inbody)
                    if report == []:
                        headers = list(parsed_body.keys())
                        report.append(headers)
                    addrow = get_vals_as_list(headers, parsed_body)
                    report.append(addrow)
                else:
                    print("Error ingesting issue for {} : error: Not a valid include file".format(valid_id))
            except Exception as e:
                    print("Error ingesting issue for {} : error: {}".format(valid_id, e))
    MU.write_csv(report, POWERBIREPORT)
    print("The PowerBI report saved to: " + POWERBIREPORT)

if __name__ == "__main__":
    main()
