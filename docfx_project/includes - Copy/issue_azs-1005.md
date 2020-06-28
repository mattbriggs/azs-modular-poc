---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-06-20
ms.author: mabrigg
ms.reviewer: kivenkat
ms.lastreviewed: nan
ms.issue-id: azs-1005
ms.sub-service: Virtual Machines

---
### VM boot diagnostics 1

- Applicable: This issue applies to all supported releases.
- Cause: When creating a new virtual machine (VM), the following error might be displayed: Failed to start virtual machine 'vm-name'. Error: Failed to update serial output settings for VM 'vm-name' . The error occurs if you enable boot diagnostics on a VM, but delete your boot diagnostics storage account.
- Remediation: Recreate the storage account with the same name you used previously.
- Occurrence: Common