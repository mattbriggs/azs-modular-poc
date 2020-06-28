'''
This script will parse and validate the current known issues includes from Azure Stack Hub
(6/27/2020).
'''

include_works = '''---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 6/28/2020
ms.author: mabrigg
ms.reviewer: kivenkat
ms.lastreviewed: nan
ms.issue-id: azs-1014
ms.sub-service: Virtual Machines

---
### VM boot diagnostics

- Applicable: This issue applies to all supported releases.
- Cause: When creating a new Windows virtual machine (VM), the following error may be displayed: Failed to start virtual machine 'vm-name'. Error: Failed to update serial output settings for VM 'vm-name' . The error occurs if you enable boot diagnostics on a VM, but delete your boot diagnostics storage account.
- Remediation: Recreate the storage account with the same name you used previously.
- Occurrence: Common
'''

include_fails = '''---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 6/28/2020
ms.author: mabrigg
ms.reviewer: kivenkat
ms.lastreviewed: nan
ms.issue-id: azs-1014
ms.sub-service: Virtual Machines

---
### VM boot diagnostics

- Applicable: This issue applies to all supported releases.
- Cause: When creating a new Windows virtual machine (VM), the following error may be displayed: Failed to start virtual machine 'vm-name'. Error: Failed to update serial output settings for VM 'vm-name' . The error occurs if you enable boot diagnostics on a VM, but delete your boot diagnostics storage account.
- Remediation: Recreate the storage account with the same name you used previously.
- Occurrence: Common
'''