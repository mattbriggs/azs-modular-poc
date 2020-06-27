---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-06-20
ms.author: mabrigg
ms.reviewer: sranthar
ms.lastreviewed: nan
ms.issue-id: azs-1029
ms.sub-service: Network

---
### Public IP

- Applicable: This issue applies to all supported releases.
- Cause: The IdleTimeoutInMinutes value for a public IP that is associated to a load balancer cannot be changed. The operation puts the public IP into a failed state.
- Remediation: To bring the public IP back into a successful state, change the IdleTimeoutInMinutes value on the load balancer rule that references the public IP back to the original value (the default value is 4 minutes).
- Occurrence: Common