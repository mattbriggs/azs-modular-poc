---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-06-20
ms.author: mabrigg
ms.reviewer: kivenkat
ms.lastreviewed: nan
ms.issue-id: azs-1010
ms.sub-service: Virtual Machines

---
### SQL VM: Auto backup cannot be configured with TLS 1.2 enabled

- Applicable: This issue applies to new installations of 2002 and later, or any previous release with TLS 1.2 enabled.
- Cause: When configuring the automated backup of SQL VMs with an existing storage account, it fails with the error SQL Server IaaS Agent: The underlying connection was closed: An unexpected error occurred on a send. 
- Remediation: nan
- Occurrence: Common