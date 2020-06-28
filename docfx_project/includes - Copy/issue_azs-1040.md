---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-06-20
ms.author: mabrigg
ms.reviewer: sranthar
ms.lastreviewed: nan
ms.issue-id: azs-1040
ms.sub-service: Network

---
### Network interface: Adding/Removing Network Interface

- Applicable: This issue applies to all supported releases.
- Cause: A new network interface cannot be added to a VM that is in a running state.
- Remediation: Stop the virtual machine before adding/removing a network interface.
- Occurrence: Common