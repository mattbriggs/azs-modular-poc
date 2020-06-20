---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-06-20
ms.author: mabrigg
ms.reviewer: kivenkat
ms.lastreviewed: nan
ms.issue-id: azs-1060
ms.sub-service: nan

---
### Capacity monitoring in SQL resource provider keeps loading

- Applicable: This issue applies to the Azure Stack Hub 1910 update or later, with SQL resource provider version 1.1.33.0 or earlier installed.
- Cause: The current version of the SQL resource provider is not compatible with some of the latest portal changes in the 1910 update.
- Remediation: Follow the resource provider update process to apply the SQL resource provider hotfix 1.1.47.0 after Azure Stack Hub is upgraded to the 1910 update ( SQL RP version 1.1.47.0 ). For the MySQL resource provider, it is also recommended that you apply the MySQL resource provider hotfix 1.1.47.0 after Azure Stack Hub is upgraded to 1910 update ( MySQL RP version 1.1.47.0 ).
- Occurrence: Common