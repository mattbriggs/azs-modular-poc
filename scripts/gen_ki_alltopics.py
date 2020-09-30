'''
Azure Stack Generate main known issues topics

9.28.2020 intial script

'''

import pandas as pd
import numpy as np
import mod_utilities

data = pd.read_csv(r"C:\git\mb\azs-modular-poc\data\reports\knownissues_report_powerbi.csv")

active_KI = data[(data["azs.status"] == 'active')]
area_KI = active_KI.groupby('Applicable to')[['ms.sub-service','azs.issue-id']]

for area in area_KI:
    releases_KI = area.groupby('Applicable to')[['ms.sub-service','azs.issue-id']]

    for release, group in releases_KI:
        print('::: moniker range="<azs-{}"'.format(release))
        section = data[(data["Applicable to"] == release)]  
        group_KI = group.groupby('ms.sub-service')[['ms.sub-service','azs.issue-id']]
        for item, sub in group_KI:
            print("\n\n## {}\n".format(item))
            for i in sub['azs.issue-id'].get_values():
                print("![INCLUDE](/azure-stack/include/{}.md)".format(i))
        print('::: moniker-end')