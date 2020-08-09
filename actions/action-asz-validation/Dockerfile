FROM python

LABEL "maintainer" = "Matt Briggs <mabrigg@microsoft.com>"

ADD val_ki_dockeraction.py /val_ki_dockeraction.py
ADD val_ki_functions.py /val_ki_functions.py
ADD mod_utilities.py /mod_utilities.py
COPY known_issue.json /known_issue.json
COPY requirements.txt /requirements.txt
COPY entrypoint.sh /entrypoint.sh

RUN pip install -r requirements.txt

ENTRYPOINT ["/entrypoint.sh"]