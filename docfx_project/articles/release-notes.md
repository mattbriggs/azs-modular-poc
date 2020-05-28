---
title: #Required; page title displayed in search results. Include the brand.
description: #Required; article description that is displayed in search results.
author: #Required; your GitHub user alias, with correct capitalization.
ms.author: #Required; microsoft alias of author; optional team alias.
ms.service: #Required; service per approved list. service slug assigned to your service by ACOM.
ms.topic: overview #Required
ms.date: #Required; mm/dd/yyyy format.
---

# Relase notes for Azure Stack Hub

This article describes the contents of Azure Stack Hub update packages. The update includes improvements and fixes for the latest release of Azure Stack Hub.

To access release notes for a different version, use the version selector dropdown above the table of contents on the left.

## Update type

The Azure Stack Hub 2002 update build type is **Full**.

The 2002 update package is larger in size compared to previous updates. The increased size results in longer download times. The update will remain in the Preparing state for a long time, and operators can expect this process to take longer than with previous updates. The 2002 update has had the following expected runtimes in our internal testing- 4 nodes: 15-42 hours, 8 nodes: 20-50 hours, 12 nodes: 20-60 hours, 16 nodes: 25-70 hours. Exact update runtimes typically depend on the capacity used on your system by tenant workloads, your system network connectivity (if connected to the internet), and your system hardware specifications. Runtimes that are shorter or longer than the expected value are not uncommon and do not require action by Azure Stack Hub operators unless the update fails. This runtime approximation is specific to the 2002 update and should not be compared to other Azure Stack Hub updates.

For more information about update build types, see [Manage updates in Azure Stack Hub](https://docs.microsoft.com/azure-stack/operator/azure-stack-updates?view=azs-2002).

## Release Notes

[!INCLUDE [notes](../includes/rel-note-01.md)]

[!INCLUDE [notes](../includes/rel-note-02.md)]

[!INCLUDE [notes](../includes/rel-note-03.md)]

## Next steps

- For an overview of the update management in Azure Stack Hub, see Manage updates in Azure Stack Hub overview.
- For more information about how to apply updates with Azure Stack Hub, see Apply updates in Azure Stack Hub.
- To review the servicing policy for Azure Stack Hub and what you must do to keep your system in a supported state, see Azure Stack Hub servicing policy.
- To use the privileged endpoint (PEP) to monitor and resume updates, see Monitor updates in Azure Stack Hub using the privileged endpoint.