---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-06-20
ms.author: mabrigg
ms.reviewer: kivenkat
ms.lastreviewed: nan
ms.issue-id: azs-1002
ms.sub-service: Virtual Machines

---
### Cannot create a VMSS with Standard_DS2_v2 VM size on portal

- Applicable: This issue applies to the 2002 release.
- Cause: There is a portal bug that prevents VMSS creation with the Standard_DS2_v2 VM size. Creating one will error out with: "{"code":"DeploymentFailed","message":"At least one resource deployment operation failed. Please list deployment operations for details. Please see https://aka.ms/arm-debug for usage details.","details":[{"code":"BadRequest","message":"{\r\n \"error\": {\r\n \"code\": \"NetworkProfileValidationError\",\r\n \"message\": \"Virtual Machine size Standard_DS2_v2 is not in the allowed list of VM sizes for accelerated networking to be enabled on the VM at index 0 for VM Scale Set /subscriptions/x/resourceGroups/RGVMSS/providers/Microsoft.Compute/virtualMachineScaleSets/vmss. Allowed sizes: .\"\r\n }\r\n}"}]}"
- Remediation: Create a VMSS with PowerShell or a resource manager template.
- Occurrence: Common