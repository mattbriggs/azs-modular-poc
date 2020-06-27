---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-06-20
ms.author: mabrigg
ms.reviewer: kivenkat
ms.lastreviewed: nan
ms.issue-id: azs-1015
ms.sub-service: Virtual Machines

---
### Virtual machine scale set: Create failures during patch and update on 4-node Azure Stack Hub environments

- Applicable: This issue applies to all supported releases.
- Cause: Creating VMs in an availability set of 3 fault domains and creating a virtual machine scale set instance fails with a FabricVmPlacementErrorUnsupportedFaultDomainSize error during the update process on a 4-node Azure Stack Hub environment.
- Remediation: You can create single VMs in an availability set with 2 fault domains successfully. However, scale set instance creation is still not available during the update process on a 4-node Azure Stack Hub
- Occurrence: nan