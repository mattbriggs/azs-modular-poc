---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-06-20
ms.author: mabrigg
ms.reviewer: kivenkat
ms.lastreviewed: nan
ms.issue-id: azs-1057
ms.sub-service: Virtual Machines

---
### Delete a storage container

- Applicable: This issue applies to all supported releases.
- Cause: In the user portal, when a user attempts to delete a storage container, the operation fails when the user does not toggle Override Azure Policy and RBAC Role settings .
- Remediation: Ensure that the box is checked for Override Azure Policy and RBAC Role settings .
- Occurrence: Common