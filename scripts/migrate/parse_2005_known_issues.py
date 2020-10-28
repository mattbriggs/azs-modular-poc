'''This script will parse the current known issues topic from Azure Stack. 
The script doesn't validate. The best approach might have been to convert.

10/14/2020

'''

from bs4 import BeautifulSoup
import markdown
from markupsafe import Markup, escape
import csv

# update variables

KNOWNISSUES = r"C:\git\mb\azs-modular-poc\data\working\2005_known_issues.md"
KNOWNISSUESTABLE = "C:\\git\\mb\\azs-modular-poc\\data\\reports\\raw_parse_2005_known_issues.csv"


def get_textfromMD(path):
    '''Return text from a MD filename path'''
    textout = ""
    fh = open(path, "r")
    for line in fh:
        textout += line
    fh.close()
    return textout


def write_csv(outbody, path):
    '''Write CSV file to the path.'''
    csvout = open(path, 'w', newline="")
    csvwrite = csv.writer(csvout)
    for r in outbody:
        try:
            csvwrite.writerow(r)
        except Exception as e:
            print("An error: {}".format(e))
    csvout.close()


def main():
    '''This is the main logic of parsing the known issues markdown file.'''
    rawtext = get_textfromMD(KNOWNISSUES)
    htmlfile = markdown.markdown(rawtext)
    soup = BeautifulSoup(htmlfile, 'html.parser')

    knownissuestable = []
    knownissuestable.append(["area", "title", "applicable", "cause", "remediation", "occurance"])

    # get area body
    body_html_string = soup.prettify()
    areas = body_html_string.split("<h2>")
    for a in areas:
        a = "<h2>" + a
        a_soup = BeautifulSoup(a,'html.parser')
        area = a_soup.findAll("h2")[0].get_text().strip()
        bodies_string = a_soup.prettify()
        bodies = bodies_string.split("<h3>")
        record = []
        for b in bodies:
            b = "<h3>" + b
            b_soup = BeautifulSoup(b,'html.parser')
            title = escape(b_soup.findAll("h3")[0].get_text().strip())
            print("Getting {}...".format(title))
            raw_body = escape(b_soup.get_text()).replace("\n", "\\n")
            raw_body = escape(b_soup.get_text()).replace("\\n\\n", "\\n")
            raw_body = " ".join(raw_body.split())
            if raw_body.find("Applicable") > 0: 
                applicable = raw_body[raw_body.find("Applicable")+11:raw_body.find("Cause")].strip()
            else:
                applicable = "NA"
            if raw_body.find("Cause") > 0:
                cause = raw_body[raw_body.find("Cause")+6:raw_body.find("Remediation")].strip()
            else:
                cause = "NA"
            if raw_body.find("Remediation") > 0:
                remediation = raw_body[raw_body.find("Remediation")+12:raw_body.find("Occurrence")].strip()
            else:
                remediation = "NA"
            if raw_body.find("Occurrence") > 0:
                index_occ_start = raw_body.find("Occurrence")+11
                index_occ_end = raw_body[index_occ_start:].find("\n")
                occurrence = raw_body[index_occ_start:index_occ_end].strip()
            else:
                occurrence = "NA"
            record = [area, title, applicable, cause, remediation, occurrence]
            knownissuestable.append(record)
    write_csv(knownissuestable, KNOWNISSUESTABLE)


if __name__ == "__main__":
    main()

