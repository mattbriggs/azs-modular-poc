'''
This script creates an Atom RSS feed using the highlights from the Known Issues.
(10/8/2020).

1. Update the DATAFILE value to point to the local reporting CSV.
2. Update the outrss to point to the folder that contains the rss feed.
3. Run the report script to get the most recent items.
4. Run the script.
5. Load the output into the RSS server.

'''
from datetime import datetime
import pandas as pd

import mod_utilities as MU

DATAFILE = r"C:\git\mb\azs-modular-poc\data\reports\knownissues_report_powerbi.csv"
OUTRSS = "C:\\git\\mb\\azs-modular-poc\\docfx_project\\rss\\WhatsNewFeed.xml"
THISDATE = str(datetime.now().strftime("%Y-%m-%d"))

def main():
    ''' Parse the include modules and create a report.'''

    # get data
    data = pd.read_csv(DATAFILE)
    active_items = data.loc[(data['azs.status'] == 'active')]
    rss_items = active_items.loc[(data['azs.highlight'] == False)]
    audience = rss_items.groupby('azs.audience')

    # create RSS file
    rss_file = ""
    rss_file += '<?xml version="1.0" encoding="utf-8"?><rss xmlns:a10="http://www.w3.org/2005/Atom" version="2.0"> <channel xmlns:slash="http://purl.org/rss/1.0/modules/slash/" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:wfw="http://wellformedweb.org/CommentAPI/" '
    for a in audience:
        groups = a[1].groupby('ms.sub-service')
        for g in groups:
            for index, row in g[1].iterrows():
                rss_file += "<item>"
                rss_file += "<title>{}</title>".format(row["title"])
                rss_file += "<link>https://azurestackhubdocs.azurewebsites.net/xml/WhatsNewFeed.xml</link>"
                rss_file += "<description>{}</description>".format(row["Description"])
                rss_file += "<language>en-us</language>"
                rss_file += "<lastBuildDate>{}</lastBuildDate>".format(THISDATE)
                rss_file += "<remedation>{}</remedation>".format(row["Remediation"])
                rss_file += "<release>{}</release>".format(row["Applicable to"])
                rss_file += "<occurance>{}</occurance>".format(row["Occurrence"])
                rss_file += '<atom:link href="https://azurestackhubdocs.azurewebsites.net/xml/WhatsNewFeed.xml" rel="self" type="application/rss+xml" />'
                rss_file += "</item>"
    rss_file += "</channel></rss>"
    print("Done.")

    MU.write_text(rss_file, OUTRSS)

if __name__ == "__main__":
    main()
