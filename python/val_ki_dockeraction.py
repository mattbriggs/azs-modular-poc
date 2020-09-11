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
SCHEMAS = r"/usr/local/bin/Model/schemas"

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
    include_paths = MU.get_files(MODULES, "md")
    print(include_paths)
    schema_paths = VAL.get_schemas(SCHEMAS)
    print(schema_paths)
    schema_set = set(schema_paths.keys())
    report = []
    report.append(["ID", "Valid", "Issue"])
    validatation_state = True
    for p in include_paths:
        split_path = p.split("\\")[-1].split("-")
        path_slug = "{}-{}".format(split_path[0],split_path[1])
        slug_index = len(path_slug)
        if path_slug in schema_set:
            in_body = MU.get_textfromMD(p)
            valid_id = p.split("\\")[-1][:-3]
            print("Validating module {} for {}".format(path_slug, valid_id[slug_index:]))
            try:
                if VAL.validate_base_file(in_body):
                    body_parse = VAL.parse_module(in_body)
                    v_line = VAL.validate_module_ki(schema_paths[path_slug], body_parse)
                    if v_line["summary"]:
                        report.append([valid_id, v_line["summary"], p, "No error."])
                    else:
                        validatation_state = False
                        fields = list(v_line["details"].keys())
                        for f in fields:
                            error_message = "{}: {}".format(v_line["details"][f][0], f)
                            report.append([valid_id, v_line["summary"], p, error_message ])
                else:
                    report.append([valid_id, False, p, "Not a valid include file."])
                    validatation_state = False
            except Exception as e:
                    report.append([valid_id, False, p, "Not a valid include file. {}".format(e)])
                    validatation_state = False
    output_table(report)
    print("The repository is valid: {}".format(validatation_state))

if __name__ == "__main__":
    main()
