---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-06-20
ms.author: mabrigg
ms.reviewer: sranthar
ms.lastreviewed: nan
ms.issue-id: azs-1025
ms.sub-service: Network

---
### ICMP protocol not supported for NSG rules

- Applicable: This issue applies to all supported releases.
- Cause: When creating an inbound or an outbound network security rule, the Protocol option shows an ICMP option. This is currently not supported on Azure Stack Hub. This issue is fixed and will not appear in the next Azure Stack Hub release. 
- Remediation: nan
- Occurrence: Common