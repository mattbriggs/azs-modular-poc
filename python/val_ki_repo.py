'''
This script will parse and validate the current known issues includes from Azure Stack Hub
(9/1/2020).

    The function validates the includes in the repository.

    1.  Configure the script by updating the global variables.
        MODULES points to the module folder.
        VALIDATIONREPORT points to the location of the validation report.
    2.  Run the script.
    3.  Open the validation report.

'''

import os
import csv
import json

import val_ki_functions as VAL
import mod_utilities as MU

MODULES = r"C:\git\mb\azs-modular-poc\docfx_project\includes"
SCHEMAS = r"C:\git\mb\azs-modular-poc\Model\schemas"
VALIDATIONREPORT = "C:\\git\\mb\\azs-modular-poc\\Data\\validation_report_validation.csv"


def main():
    '''
        Validate includes in the repo. (Main Logic for repo parsing)
    '''
    include_paths = MU.get_files(MODULES, "md")
    schema_paths = VAL.get_schemas(SCHEMAS)
    schema_set = set(schema_paths.keys())
    print(schema_set)
    report = []
    report.append(["issueid", "validation status", "path", "error"])
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
