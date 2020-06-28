'''Validation functions.'''

import cerberus as CB


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


def validate_summary(schema, indict):
    v = CB.Validator(schema)
    v.require_all = True
    v.allow_unknown = True
    valid_check = v.validate(indict)
    valid_return = {}
    valid_return["summary"] = valid_check
    valid_return["details"] = v.errors
    return valid_return


def main():
    print("This is the base module for include validation.")

if __name__ == "__main__":
    main()

