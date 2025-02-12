
ibm_pi_network_security_group_action -- Configure IBM Cloud 'ibm_pi_network_security_group_action' resource
===========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_network_security_group_action' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pi_network_security_group_action

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  pi_action (True, str, None)
    (Required for new resource) Name of the action to take; can be enable to enable NSGs in a workspace or disable to disable NSGs in a workspace.


  pi_cloud_instance_id (True, str, None)
    (Required for new resource) The GUID of the service instance associated with an account.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  zone (False, str, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environment variable 'IC_ZONE'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

