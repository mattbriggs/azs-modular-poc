---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-06-20
ms.author: mabrigg
ms.reviewer: kivenkat
ms.lastreviewed: nan
ms.issue-id: azs-1049
ms.sub-service: Virtual Machines

---
### Create Managed Disk snapshot

- Applicable: This issue applies to release 2002.
- Cause: In the user portal, when creating a Managed Disk snapshot, the Account type box is empty. When you select the Create button with an empty account type, the snapshot creation fails.
- Remediation: Select an account type from the Account type dropdown list, then create the snapshot.
- Occurrence: Common