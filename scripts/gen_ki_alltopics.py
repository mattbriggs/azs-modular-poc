'''4567890123456789012345678901234567890123456789012345678901234567890

Azure Stack Generate individual rp topiocs

You can find the sketch of this process at: 2020.6.18 - Initial
Publication Process in the AzS Hub Content Strategy OneNote.

10.1.2020 intial script

'''

from datetime import datetime
import pandas as pd
import numpy as np

import mod_utilities as MU

# variable block

DATAFILE = r"C:\git\mb\azs-modular-poc\data\reports\knownissues_report_powerbi.csv"
TARGETBASE = "C:\\git\\mb\\azs-modular-poc\\docfx_project\\articles\\"
THISDATE = str(datetime.now().strftime("%Y-%m-%d"))


def build_top_block(RP):
    '''Build the top section of the file.'''

    metadatablock = '''---
title: Azure Stack Hub known issues for {} (POC)
description: Learn about known issues in Azure Stack Hub releases.
author: sethmanheim

ms.topic: article
ms.date: {}
ms.author: sethm
ms.reviewer: sranthar
ms.lastreviewed: {}
---

# Azure Stack Hub known issues for {}

This article lists known issues in releases of Azure Stack Hub. The list is updated as new issues are identified.

'''.format(RP, RP, THISDATE, THISDATE)

    return metadatablock

def build_end_block():
    '''Build the end markdown section of the file.'''

    endblock = '''
## Archive

To access archived known issues for an older version, use the version selector dropdown above the table of contents on the left, and select the version you want to see.

## Next steps

- [Review update activity checklist](release-notes-checklist.md)
- [Review list of security updates](release-notes-security-updates.md)
'''
    return endblock


def build_known_issues():
    ''' '''
    data = pd.read_csv(DATAFILE)

    active_items = data.loc[(data['azs.status'] == 'active')]
    rp = active_items[['azs.audience', 'ms.sub-service', 'Applicable to', 'azs.issue-id']]

    audience = rp.groupby('azs.audience')
    for a in audience:
        a_stem = a[0].lower()
        print(a_stem)
        groups = a[1].groupby('ms.sub-service')
        for g in groups:
            rp_stem = g[0].replace(" ", "-").lower()
            file_name = "target/{}/{}.md".format(a_stem, rp_stem)
            print(file_name)
            print("-- start file -- \n")
            releases = g[1].groupby('Applicable to')
            for r in releases:
                print('::: moniker range="<azs-{}"'.format(r[0]))
                items = r[1].groupby('azs.issue-id')
                for i in items:
                    print("![INCLUDE](/azure-stack/include/{}0.md".format(i[0]))
                print("::: moniker-end")
            print("-- end file -- \n")

def main():
    '''Build and save the RP files.'''
    build_known_issues()

if __name__ == "__main__":
    main()
