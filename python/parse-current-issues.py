'''This script will parse the current known issues topic from Azure Stack (6/16/2020).'''

from bs4 import BeautifulSoup
import markdown
from markupsafe import Markup, escape
import csv

# update variables

KNOWNISSUES = r"C:\git\mb\azs-modular-poc\python\data\preparse.md"
KNOWNISSUESTABLE = "C:\\git\\mb\\azs-modular-poc\\python\\data\\knownissues.csv"


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
    rawtext =  get_textfromMD(KNOWNISSUES)
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
            raw_body = escape(b_soup.get_text()).replace("\n", " ")
            raw_body = " ".join(raw_body.split())
            applicable = raw_body[raw_body.find("Applicable")+11:raw_body.find("Cause")].strip()
            cause = raw_body[raw_body.find("Cause")+6:raw_body.find("Remediation")].strip()
            remediation = raw_body[raw_body.find("Remediation")+12:raw_body.find("Occurrence")].strip()
            occurance = raw_body[raw_body.find("Occurrence")+11:].strip()
            record = [area, title, applicable, cause, remediation, occurance]
            knownissuestable.append(record)
    write_csv(knownissuestable, KNOWNISSUESTABLE)


if __name__ == "__main__":
    main()

