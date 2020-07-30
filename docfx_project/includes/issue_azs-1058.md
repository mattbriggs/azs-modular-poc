---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-06-20
ms.author: mabrigg
ms.reviewer: kivenkat
ms.lastreviewed: nan
ms.issue-id: azs-1058
ms.sub-service: Virtual Machines

---
### Refresh button on virtual machines fails

- Applicable: This issue applies to all supported releases.
- Cause: In the user portal, when you navigate to Virtual Machines and try to refresh using the button at the top, the states fail to update accurately.
- Remediation: The status is automatically updated every 5 minutes regardless of whether the refresh button has been clicked or not. Wait 5 minutes and check the status.
- Occurrence: Common