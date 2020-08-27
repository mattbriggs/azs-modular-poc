'''4567890123456789012345678901234567890123456789012345678901234567890

Azure Stack Generate main known issues topic

You can find the sketch of this process at: 2020.6.18 - Initial
Publication Process in the AzS Hub Content Strategy OneNote.

6.20.2020 intial script
8.14.2020 updated to include current schema

'''

from datetime import datetime
import csv
import pandas as pd
import numpy as np

import mod_utilities as MU

# variable block

DATAFILE = r"C:\git\mb\azs-modular-poc\python\data\knownissues_report_powerbi.csv"
TARGET = "C:\\git\\mb\\azs-modular-poc\\docfx_project\\articles\\known-issues-poc.md"
THISDATE = str(datetime.now().strftime("%Y-%m-%d"))

# template block

metadatablock = '''---
title: Azure Stack Hub known issues (POC)
description: Learn about known issues in Azure Stack Hub releases.
author: sethmanheim

ms.topic: article
ms.date: {}
ms.author: sethm
ms.reviewer: sranthar
ms.lastreviewed: {}
---

# Azure Stack Hub known issues

This article lists known issues in releases of Azure Stack Hub. The list is updated as new issues are identified.

'''.format(THISDATE, THISDATE)

endblock = '''
## Archive

To access archived known issues for an older version, use the version selector dropdown above the table of contents on the left, and select the version you want to see.

## Next steps

- [Review update activity checklist](release-notes-checklist.md)
- [Review list of security updates](release-notes-security-updates.md)
'''

def main():
    '''Get the datafile, drop fields, get 'ready', and then loop
    through the list to create the markdown files.'''

    data = pd.read_csv(DATAFILE)
    active_KI = data[(data["azs.status"] == 'active')]
    group_KI = active_KI.groupby('ms.sub-service')[['ms.sub-service','azs.issue-id']]

    # build markdown
    print("Starting build.")
    knownissuesfile = metadatablock
    for name, group in group_KI:
        feature_area = "\n\n## {}\n".format(name)
        print("Getting issues for {}...\n".format(feature_area))
        knownissuesfile += feature_area
        for i in group['azs.issue-id'].get_values():
            issue = "[!INCLUDE [notes] (../includes/{}.md)]\n".format(i)
            knownissuesfile += issue
    knownissuesfile += endblock
    MU.write_text(knownissuesfile, TARGET)

    print("\nBuild done.")

if __name__ == "__main__":
    main()
