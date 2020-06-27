---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-06-20
ms.author: mabrigg
ms.reviewer: kivenkat
ms.lastreviewed: nan
ms.issue-id: azs-1007
ms.sub-service: Virtual Machines

---
### Consumed compute quota

- Applicable: This issue applies to all supported releases.
- Cause: When creating a new virtual machine, you may receive an error such as This subscription is at capacity for Total Regional vCPUs on this location. This subscription is using all 50 Total Regional vCPUs available. . This indicates that the quota for total cores available to you has been reached.
- Remediation: Ask your operator for an add-on plan with additional quota. Editing the current plan's quota will not work or reflect increased quota.
- Occurrence: Rare