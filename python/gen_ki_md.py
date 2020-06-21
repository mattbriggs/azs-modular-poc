'''4567890123456789012345678901234567890123456789012345678901234567890

Azure Stack Hub Known Issues - Publication Process for markdown

You can find the sketch of this process at: 2020.6.18 - Initial
Publication Process in the AzS Hub Content Strategy OneNote.

6.20.2020

'''

from datetime import datetime
import html
import pandas as pd


# variable block

DATAFILE = r"C:\git\mb\azs-modular-poc\python\data\creeb_azsknownissues.csv"
TARGET = "C:\\git\\mb\\azs-modular-poc\\docfx_project\\includes\\"
STEM = "issue_"
THISDATE = str(datetime.now().strftime("%Y-%m-%d"))


def build_include(inlist):
    '''Build the markdown as a string'''

    # get alais only for ms.reviewer
    if inlist[0].find("@") > 0:
        msreviewer = inlist[0].split("@")[0]
    else:
        msreviewer = inlist[0]

    includefile = '''---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: {}
ms.author: mabrigg
ms.reviewer: {}
ms.lastreviewed: {}
ms.issue-id: {}
ms.sub-service: {}

---
### {}

- Applicable: {}
- Cause: {}
- Remediation: {}
- Occurrence: {}'''.format(THISDATE, msreviewer, inlist[4],
    inlist[1], inlist[5], inlist[8], inlist[7], inlist[9], 
    inlist[10], inlist[11])
    includefile = html.unescape(includefile)
    return includefile


def write_text(outbody, path):
    '''Write text file to the path.'''
    out_file = open(path, "w")
    for line in outbody:
        out_file.write(line)
    out_file.close()


def get_data_from_csv(path):
    '''Get data and order'''
    data = pd.read_csv(path)
    issues = data.drop(["importsequencenumber", "statuscode", "statecode",
        "timezoneruleversionnumber", "utcconversiontimezonecode",
        "versionnumber", "owningbusinessunit", 
        "creeb_trackingnumber"], axis=1)
    issues = issues[issues["creeb_status"] == "Ready" ]
    issuesorder = issues[["creeb_contact", "creeb_id",
        "creeb_status", "creeb_datefiled", "creeb_datereviewed",
        "creeb_feature", "creeb_audience", "creeb_applicable",
        "creeb_title", "creeb_cause", "creeb_remediation",
        "creeb_occurance"]]
    listofissues = issuesorder.values.tolist()

    return listofissues



def main():
    '''Get the datafile, drop fields, get 'ready', and then loop
    through the list to create the markdown files.'''

    listofissues = get_data_from_csv(DATAFILE)

    # build markdown
    print("Starting build.")
    for i in listofissues:
        print("Writing ... {}".format(i[1]))
        filenamepath = "{}{}{}.md".format(TARGET, STEM, i[1])
        filebody = build_include(i)
        try:
            write_text(filebody, filenamepath)
        except Exception as e:
            print("Error writing {}\n     {}".format(i[1],e))
    print("\nBuild done.")


if __name__ == "__main__":
    main()
