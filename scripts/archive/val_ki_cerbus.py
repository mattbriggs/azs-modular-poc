import cerberus as CB

def valid_check(document, schema):
    v = CB.Validator(schema)
    return v.validate(document)

schema = {'name': {'type': 'string'}}
document = {'name': 'john doe'}

schema1 = {'author': {'type': 'string'}, 'ms.service': {'type': 'string'}, 'ms.date': {'type': 'string'}, 'ms.lastreviewed': {'type': 'string'}, 'ms.topic': {'type': 'string'}, 'ms.author': {'type': 'string'}, 'ms.reviewer': {'type': 'string'}, 'ms.issue-id': {'type': 'string'}, 'ms.sub-service': {'type': 'string'}, 'title': {'type': 'string'}, 'Applicable': {'type': 'string'}, 'Cause': {'type': 'string'}, 'Remediation': {'type': 'string'}, 'Occurrence': {'type': 'string'} }

document1 = {'title': 'VM boot diagnostics',
 'Applicable': 'This issue applies to all supported releases.',
  'Cause': "When creating a new Windows virtual machine (VM), the following error may be displayed: Failed to start virtual machine 'vm-name'. Error: Failed to update serial output settings for VM 'vm-name' . The error occurs if you enable boot diagnostics on a VM, but delete your boot diagnostics storage account.",
'Remediation': 'Recreate the storage account with the same name you used previously.',
'Occurrence': 'Common',
'ms.service': 'azure-stack',
'ms.date' : '9/10/2020',
'author' : 'mabrigg', 
'ms.topic': 'include',
'ms.author': 'mabrigg',
'ms.reviewer': 'kivenkat',
'ms.lastreviewed': 'nan', 
'ms.issue-id': 'azs-1014',
'ms.sub-service': 'Virtual Machines'}

schema2 = {'name': {'type': 'string', 'maxlength': 10}}
document2 = {'name': 'john', 'sex': 'M'}

v = CB.Validator()
v.require_all = True
print(v.validate(document1, schema1))
print(v.errors)