---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-06-20
ms.author: mabrigg
ms.reviewer: avishwan
ms.lastreviewed: nan
ms.issue-id: azs-1071
ms.sub-service: Patch and Update

---
### Update fails

- Applicable: This issue applies to all supported releases.
- Cause: When attempting to install the 1907 Azure Stack Hub update, the status for the update might fail and change state to PreparationFailed . This is caused by the update resource provider (URP) being unable to properly transfer the files from the storage container to an internal infrastructure share for processing.
- Remediation: Starting with version 1901 (1.1901.0.95), you can work around this issue by clicking Update now again (not Resume ). The URP then cleans up the files from the previous attempt, and restarts the download. If the problem persists, we recommend manually uploading the update package by following the Import and install updates section .
- Occurrence: Common