---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-06-20
ms.author: mabrigg
ms.reviewer: avishwan
ms.lastreviewed: nan
ms.issue-id: azs-1067
ms.sub-service: SQL and MySQL

---
### SQL/MySQL

- Applicable: This issue applies to release 2002.
- Cause: If the stamp contains SQL resource provider (RP) version 1.1.33.0 or earlier, upon update of the stamp, the blades for SQL/MySQL will not load.
- Remediation: Update the RP to version 1.1.47.0
- Occurrence: nan