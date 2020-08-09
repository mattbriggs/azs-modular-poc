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
import json

import val_ki_functions as VAL
import mod_utilities as MU
from prettytable import PrettyTable

MODULES = r"/usr/local/azs-modular-poc/docfx_project/includes"
SCHEMA = r"/usr/local/bin/known_issue.json"

def repo_logic(indict):
    '''Insert the logic to process the return from the function.'''
    print(indict)

def output_table(inmatrix):
    '''With the list in a list print a list for pretty print'''
    x = PrettyTable()
    x.field_names = inmatrix[0]
    for inx, row in enumerate(inmatrix):
        if inx > 0:
            x.add_row(row)
    x.align = "l"
    print(x)

def main():
    '''
        Validate includes in the repo. (Main Logic for repo parsing)
    '''
    include_path = MU.get_files(MODULES)
    report = []
    report.append(["ID", "Valid", "Issue"])
    for p in include_path:
        if p.find("issue_azs") > -1:
            inbody = MU.get_textfromMD(p)
            valid_id = p.split("//")[-1][:-3]
            try:
                if VAL.validate_base_file(inbody):
                    v_line = VAL.validate_module_ki(SCHEMA, inbody)
                    if v_line["summary"]:
                        report.append([valid_id, v_line["summary"], "No issue."])
                    else:
                        fields = list(v_line["details"].keys())
                        for f in fields:
                            error_message = "{}: {}".format(v_line["details"][f][0], f)
                            report.append([valid_id, v_line["summary"], error_message ])
                else:
                    report.append([valid_id, False, "Not a valid module file."])
            except Exception as e:
                    report.append([valid_id, False,"Not a valid module file. {}".format(e)])
    output_table(report)

if __name__ == "__main__":
    main()
