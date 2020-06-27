---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-06-20
ms.author: mabrigg
ms.reviewer: kivenkat
ms.lastreviewed: nan
ms.issue-id: azs-1009
ms.sub-service: Virtual Machines

---
### SQL VM: Storage account creating failure when configuring Auto Backup

- Applicable: This issue applies to 2002.
- Cause: When configuring the automated backup of SQL VMs with a new storage account, it fails with the error Deployment template validation failed. The template parameter for 'SqlAutobackupStorageAccountKind' is not found.
- Remediation: Apply the latest 2002 hotfix.
- Occurrence: nan