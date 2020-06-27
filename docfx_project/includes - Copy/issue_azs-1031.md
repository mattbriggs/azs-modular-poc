---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-06-20
ms.author: mabrigg
ms.reviewer: sranthar
ms.lastreviewed: nan
ms.issue-id: azs-1031
ms.sub-service: Network

---
### Load balancer

- Applicable: This issue applies to all supported releases.
- Cause: When adding availability set VMs to the backend pool of a load balancer, an error message is displayed on the portal stating Failed to save load balancer backend pool . This is a cosmetic issue on the portal; the functionality is still in place and VMs are successfully added to the backend pool internally. 
- Remediation: nan
- Occurrence: Common