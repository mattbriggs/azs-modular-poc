---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-08-14
ms.author: mabrigg
ms.reviewer: kivenkat
ms.lastreviewed: 2020-08-14
ms.sub-service: Virtual Machines
azs.tracking: 123456
azs.issue-id: known-issue-ea0a8111-eab0-ea11-a812-000d3a5465d8
azs.status: ready
azs.topic-schema: known-issue
azs.audience: Operator
azs.highlight: False
---
### SQL VM: Auto backup cannot be configured with TLS 1.2 enabled

- Applicable to: This issue applies to new installations of 2002 and later, or any previous release with TLS 1.2 enabled.
- Description: When configuring the automated backup of SQL VMs with an existing storage account, it fails with the error SQL Server IaaS Agent: The underlying connection was closed: An unexpected error occurred on a send. 
- Remediation: NA
- Occurrence: Common