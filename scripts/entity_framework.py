'''Draft of the entity framework took.'''

%% Azure Stack Hub Content Model V0.1 9.13.2020

class BaseModule():
    
    Base_module -- Sub_service
    Base_module -- Azs_status
    Base_module -- Azs_audience
    Base_module : String author
    Base_module : String ms.service
    Base_module : String ms.topic
    Base_module : String ms.date
    Base_module : String ms.author
    Base_module : String ms.reviewer
    Base_module : String ms.lastreviewed
    Base_module : enum sub_service
    Base_module : String azs.tracking
    Base_module : String azs.module_id
    Base_module : enum Azs_status
    Base_module : String azs.topic_schema
    Base_module : enum  Azs_audience
    Base_module : bool azs.highlight
    class Known_issue{
        String applicable_to
        String description
        String remediation
        String occurance
    }
    class Whats_new{
        String applicable_to
        String description
        String for_more_information
    }
    class Sub_service{
        %% enumeration
        Advisory
        Alerts, Health Monitoring and Hardware
        App Services
        Backup and Disaster Recovery
        Billing or Usage Tracking
        Cloud Operator Issues
        Deployment
        Registration of Azure Stack
        Development Kit ASDK
        Marketplace Mgmt.
        Network
        Patch and Update
        Plans, Offers, Quota, or Subscriptions
        Security, Certificate and Secret Management, Support, Monitoring
        SQL MySQL
        Storage
        Tools and SDK
        Virtual Machines
        PowerShell, Developer Tools, SDKs
        Validation as a Service
        Release Notes
        Kubernetes
        Add on RPs
        Solutions for Azure Stack Hub
        Developer using Azure Stack Hub
        Rugged Devices
    }
    class Azs_status{
        %% enumeration
        Ready
        In_review
        Archive
    }
    class Azs_audience{
        %% enumeration
        User
        Operator
    }

    
