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

import pandas as pd

DATAFILE = r"C:\git\mb\azs-modular-poc\data\reports\knownissues_report_powerbi.csv"

def main():
    ''' Parse the include modules and create a report.'''
    data = pd.read_csv(DATAFILE)
    active_items = data.loc[(data['azs.status'] == 'active')]
    rss_items = active_items.loc[(data['azs.highlight'] == False)]
    audience = rss_items.groupby('azs.audience')
    print('<?xml version="1.0" encoding="UTF-8" ?><rss version="2.0"><channel><title>POC RSS for Azure Stack Hub</title><link>https://docs.microsoft.com/azure-stack</link><description>An RSS of Known Issues for Azure Stack Hub</description>')
    for a in audience:
        print("<audience>{}".format(a[0]))
        groups = a[1].groupby('ms.sub-service')
        for g in groups:
            print("<area>{}".format(g[0]))
            for index, row in g[1].iterrows():
                print("<item>")
                print("<title>{}</title>".format(row["title"]))
                print("<description>{}</description>".format(row["Description"]))
                print("<remedation>{}</remedation>".format(row["Remediation"]))
                print("<release>{}</release>".format(row["Applicable to"]))
                print("<occurance>{}</occurance>".format(row["Occurrence"]))
                print("</item>")
            print("</area>")
        print("</audience>")

if __name__ == "__main__":
    main()
