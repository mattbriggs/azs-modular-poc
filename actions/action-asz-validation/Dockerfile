FROM python

LABEL "maintainer" = "Matt Briggs <mabrigg@microsoft.com>"

ADD val_ki_dockeraction.py /usr/local/bin/val_ki_dockeraction.py
ADD val_ki_functions.py /usr/local/bin/val_ki_functions.py
ADD mod_utilities.py /usr/local/bin/mod_utilities.py
COPY known_issue.json /usr/local/bin/known_issue.json
COPY requirements.txt /usr/local/bin/requirements.txt
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

RUN pip install -r /usr/local/bin/requirements.txt

ENTRYPOINT ["bash", "/usr/local/bin/entrypoint.sh"]