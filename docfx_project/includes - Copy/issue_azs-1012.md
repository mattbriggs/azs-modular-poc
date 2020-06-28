---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-06-20
ms.author: mabrigg
ms.reviewer: kivenkat
ms.lastreviewed: nan
ms.issue-id: azs-1012
ms.sub-service: Virtual Machines

---
### Privileged Endpoint

- Applicable: This issue applies to 1910 and earlier releases.
- Cause: Unable to connect to the Privileged Endpoint (ERC VMs) from a computer running a non-English version of Windows.
- Remediation: This is a known issue that has been fixed in releases later than 1910. As a workaround you can run the New-PSSession and Enter-PSSession PowerShell cmdlets using the en-US culture; for examples, set the culture using this script: https://resources.oreilly.com/examples/9780596528492/blob/master/Use-Culture.ps1.
- Occurrence: Rare