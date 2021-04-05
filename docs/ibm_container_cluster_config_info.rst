
ibm_container_cluster_config_info -- Retrieve IBM Cloud 'ibm_container_cluster_config' resource
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_container_cluster_config' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.23.0
- Terraform v0.12.20



Parameters
----------

  download (False, bool, True)
    If set to false will not download the config, otherwise they are downloaded each time but onto the same path for a given cluster name/id


  admin (False, bool, False)
    If set to true will download the config for admin


  config_dir (False, str, None)
    The directory where the cluster config to be downloaded. Default is home directory


  network (False, bool, False)
    If set to true will download the Calico network config with the Admin config


  cluster_name_id (True, str, None)
    The name/id of the cluster


  resource_group_id (False, str, None)
    ID of the resource group.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

