''' Quick and dirty validator and syndicator

# 1. convert into a json object (model)
# 2. Validate the json object using rules.
# 3. Convert to object
# 4. Convert to RSS.

v0.1 5.28.2020

'''
import os
import datetime
from bs4 import BeautifulSoup
import markdown
import rfeed as rss
import uuid


def get_text_from_file(path):
    '''Return text from a text filename path'''
    textout = ""
    fh = open(path, "r")
    for line in fh:
        textout += line
    fh.close()
    return textout


def get_files(inpath, "md"):
    '''With the directory path, returns a list of markdown file paths.'''
    outlist = []
    for (path, dirs, files) in os.walk(inpath):
        for filename in files:
            ext_index = filename.find(".")
            if filename[ext_index+1:] == "md":
                entry = path + "\\" + filename
                outlist.append(entry)
    return outlist


def clear_docs_repo_metadata(inrawbody, d_format="html"):
    '''With raw markdown file and docs metadata block, turn just the body as the indicated
    format, html, text, or markown'''
    # clear metadata block
    meta_flag = "---"
    mleng = len(meta_flag)
    meta_end = inrawbody[inrawbody.find(meta_flag)+mleng:].find(meta_flag)+(mleng*2)
    body = inrawbody[meta_end:]
    # clear Next steps
    if body.find("## Next steps") > -1:
        body_halves = body.split("## Next steps")
        body = body_halves[0]

    # clear code blocks
    body_lines = body.split("\n")
    body_strip = []
    state = False
    for l in body_lines:
        if state == True and l.find("```") > -1:
            state = False
        elif state == False and l.find("```") > -1:
            state = True
        elif state == False:
            body_strip.append(l)
    body = "\n".join(body_strip)
    if d_format == "html":
        out_file = markdown.markdown(body)
    elif d_format == "txt":
        html_doc = markdown.markdown(body)
        soup = BeautifulSoup(html_doc, 'html.parser')
        out_file = soup.get_text()
    else:
        out_file = body
    return out_file


def convert_rss_obj(inbody):
    '''Provisional function to return RSS object for each include.'''
    # soup = BeautifulSoup(inbody, 'html.parser')
    # description = soup.prettify()
    this_item = str(uuid.uuid4())
    item = rss.Item(description = inbody, guid = rss.Guid(this_item))
    return item


def main():
    print("This is the initial validation and RSS convertor script.")
    includes = get_files("./docfx_project/includes")
    out_items = []
    for i in includes:
        body = get_text_from_file(i)
        body_html = clear_docs_repo_metadata(body, d_format="txt")
        out_items.append(convert_rss_obj(body_html))

    feed = rss.Feed(
        title = "Example RSS Feed",
        link = "http://docs.microsoft.com/azure-stack/rss",
        description = "Release notes for Azure Stack Hub.",
        language = "en-US",
        lastBuildDate = datetime.datetime.now(),
        items = out_items
    )

    print(feed.rss())

if __name__ == "__main__":
    main()
