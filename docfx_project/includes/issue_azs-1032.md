---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-06-20
ms.author: mabrigg
ms.reviewer: sranthar
ms.lastreviewed: nan
ms.issue-id: azs-1032
ms.sub-service: Network

---
### Network Security Groups

- Applicable: This issue applies to all supported releases.
- Cause: An explicit DenyAllOutbound rule cannot be created in an NSG as this will prevent all internal communication to infrastructure needed for the VM deployment to complete. 
- Remediation: nan
- Occurrence: Common