---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-06-20
ms.author: mabrigg
ms.reviewer: kivenkat
ms.lastreviewed: nan
ms.issue-id: azs-1046
ms.sub-service: nan

---
### Administrative subscriptions

- Applicable: This issue applies to all supported releases.
- Cause: The two administrative subscriptions that were introduced with version 1804 should not be used. The subscription types are Metering subscription, and Consumption subscription.
- Remediation: If you have resources running on these two subscriptions, recreate them in user subscriptions.
- Occurrence: Common