---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-06-20
ms.author: mabrigg
ms.reviewer: kivenkat
ms.lastreviewed: nan
ms.issue-id: azs-1061
ms.sub-service: nan

---
### SQL resource provider

- Applicable: This issue applies to stamps that are running 1908 or earlier.
- Cause: When deploying the SQL resource provider (RP) version 1.1.47.0, the portal shows no assets other than those associated with the SQL RP.
- Remediation: Delete the RP, upgrade the stamp, and re-deploy the SQL RP
- Occurrence: nan