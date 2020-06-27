---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-06-20
ms.author: mabrigg
ms.reviewer: kivenkat
ms.lastreviewed: nan
ms.issue-id: azs-1006
ms.sub-service: Virtual Machines

---
### VM boot diagnostics 2

- Applicable: This issue applies to all supported releases.
- Cause: When trying to start a stop-deallocated virtual machine,the following error might be displayed: VM diagnostics Storage account 'diagnosticstorageaccount' not found. Ensure storage account is not deleted . The error occurs if you attempt to start a VM with boot diagnostics enabled, but the referenced boot diagnostics storage account is deleted.
- Remediation: Recreate the storage account with the same name you used previously.
- Occurrence: Common