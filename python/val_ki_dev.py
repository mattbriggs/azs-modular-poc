'''Working through validation logic.'''

import cerberus as CB

include = '''---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-06-20
ms.author: mabrigg
ms.reviewer: kivenkat
ms.lastreviewed: nan
ms.issue-id: azs-1014
ms.sub-service: Virtual Machines

---
### VM boot diagnostics

- Applicable: This issue applies to all supported releases.
- Cause: When creating a new Windows virtual machine (VM), the following error may be displayed: Failed to start virtual machine 'vm-name'. Error: Failed to update serial output settings for VM 'vm-name' . The error occurs if you enable boot diagnostics on a VM, but delete your boot diagnostics storage account.
- Occurrence: Common
'''

schema_include = {'author': {'type': 'string'},
'ms.service': {'type': 'string'},
'ms.date': {'type': 'string'},
'ms.lastreviewed': {'type': 'string'},
'ms.topic': {'type': 'string'},
'ms.author': {'type': 'string'},
'ms.reviewer': {'type': 'string'},
'ms.issue-id': {'type': 'string'},
'ms.sub-service': {'type': 'string'},
'title': {'type': 'string'},
'Applicable': {'type': 'string'},
'Cause': {'type': 'string'},
'Remediation': {'type': 'string'},
'Occurrence': {'type': 'string'}
}


def validate_base_file(rawbody):
    '''With a file incoming check that is really markdown with a metadata block.'''
    base_valid = {}
    sections = rawbody.split("---\n")
    if len(sections) == 3:
        base_valid["metablock"] = True
    else:
        base_valid["metablock"] = False
    #summary
    if False in base_valid.values():
        base_valid["valid"] = False
    else:
        base_valid["valid"] = True
    return base_valid


def parse_include(inbody, include_head, tokens):
    '''Method parses an include file.'''

    # break body
    parts = inbody.split("---\n")
    elements = parts[2].split("- ")

    # get body
    elements_dict = {}
    elements_dict["title"] = elements[0].split(include_head + " ")[1].strip()
    for indx, e in enumerate(elements):
        if indx > 0:
            for t in tokens:
                if e.find(t) > -1:
                    elements_dict[t] =e.split(t + ":")[1].strip()

    # get metadata
    metadata_lines = parts[1].split("\n")
    for i in metadata_lines:
        if i.find(":") > -1:
            bits = i.split(":")
            key = bits[0].strip()
            value = bits[1].strip()
            elements_dict[key] = value

    return elements_dict


def validate_summary(indict, schema):
    v = CB.Validator(schema)
    v.allow_unknown = True
    valid_check = v.validate(indict)
    valid_return = {}
    valid_return["summary"] = valid_check
    valid_return["details"] = v.errors
    return valid_return

include_head = "###"
tokens = ["Applicable", "Cause", "Remediation", "Occurrence"]
include_body = parse_include(include, include_head, tokens)
print(include_body)
print(validate_summary(include_body, schema_include))
