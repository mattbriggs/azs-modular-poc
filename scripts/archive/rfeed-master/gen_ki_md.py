'''4567890123456789012345678901234567890123456789012345678901234567890

Azure Stack Hub Known Issues - Publication Process for markdown

You can find the sketch of this process at: 2020.6.18 - Initial
Publication Process in the AzS Hub Content Strategy OneNote.

6.20.2020 intial script
8.14.2020 updated to include current schema

'''

from datetime import datetime
import html
import csv

# variable block

DATAFILE = r"C:\git\mb\azs-modular-poc\data\reports\creeb_azsknownissues.csv"
TARGET = "C:\\git\\mb\\azs-modular-poc\\docfx_project\\includes\\"
STEM = "known-issue"
THISDATE = str(datetime.now().strftime("%Y-%m-%d"))


def build_include(inlist):
    '''Build the markdown as a string'''

    # get alais only for ms.reviewer
    if inlist[4].find("@") > 0:
        msreviewer = inlist[4].split("@")[0]
    else:
        msreviewer = inlist[4]

    includefile = '''---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: {}
ms.author: mabrigg
ms.reviewer: {}
ms.lastreviewed: 2020-08-14
ms.sub-service: {}
azs.tracking: 123456
azs.issue-id: {}-{}
azs.status: active
azs.topic-schema: known-issue
azs.audience: Operator
azs.highlight: False
---
### {}

- Applicable to: {}
- Description: {}
- Remediation: {}
- Occurrence: {}'''.format(THISDATE, msreviewer, inlist[7], STEM,
    inlist[2], inlist[16], inlist[0], inlist[3], inlist[12], inlist[11])
    includefile = html.unescape(includefile)
    return includefile


def write_text(outbody, path):
    '''Write text file to the path.'''
    out_file = open(path, "w")
    for line in outbody:
        out_file.write(line)
    out_file.close()


def main():
    '''Get the datafile, drop fields, get 'ready', and then loop
    through the list to create the markdown files.'''

    with open(DATAFILE, 'r') as f:
        reader = csv.reader(f)
        listofissues = list(reader)
        
    # build markdown
    print("Starting build.")
    for inx, i in enumerate(listofissues):
        if inx > 0:
            print("Writing ... {}".format(i[1]))
            filenamepath = "{}{}-{}.md".format(TARGET, STEM, i[2])
            filebody = build_include(i)
            try:
                write_text(filebody, filenamepath)
            except Exception as e:
                print("Error writing {}\n     {}".format(i[1],e))
    print("\nBuild done.")


if __name__ == "__main__":
    main()
