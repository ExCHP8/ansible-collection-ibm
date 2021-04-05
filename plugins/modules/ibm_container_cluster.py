#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_container_cluster
short_description: Configure IBM Cloud 'ibm_container_cluster' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_container_cluster' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.23.0
    - Terraform v0.12.20

options:
    public_vlan_id:
        description:
            - Public VLAN ID
        required: False
        type: str
    service_subnet:
        description:
            - Custom subnet CIDR to provide private IP addresses for services
        required: False
        type: str
    resource_group_id:
        description:
            - ID of the resource group.
        required: False
        type: str
    tags:
        description:
            - Tags for the resource
        required: False
        type: list
        elements: str
    subnet_id:
        description:
            - List of subnet IDs
        required: False
        type: list
        elements: str
    default_pool_size:
        description:
            - The size of the default worker pool
        required: False
        type: int
        default: 1
    labels:
        description:
            - list of labels to the default worker pool
        required: False
        type: dict
        elements: str
    wait_for_worker_update:
        description:
            - Wait for worker node to update during kube version update.
        required: False
        type: bool
        default: True
    wait_till:
        description:
            - wait_till can be configured for Master Ready, One worker Ready or Ingress Ready
        required: False
        type: str
        default: IngressReady
    no_subnet:
        description:
            - Boolean value set to true when subnet creation is not required.
        required: False
        type: bool
        default: False
    patch_version:
        description:
            - Kubernetes patch version
        required: False
        type: str
    update_all_workers:
        description:
            - Updates all the woker nodes if sets to true
        required: False
        type: bool
        default: False
    entitlement:
        description:
            - Entitlement option reduces additional OCP Licence cost in Openshift Clusters
        required: False
        type: str
    name:
        description:
            - (Required for new resource) The cluster name
        required: True
        type: str
    public_service_endpoint:
        description:
            - None
        required: False
        type: bool
    webhook:
        description:
            - None
        required: False
        type: list
        elements: dict
    datacenter:
        description:
            - (Required for new resource) The datacenter where this cluster will be deployed
        required: True
        type: str
    kms_config:
        description:
            - Enables KMS on a given cluster
        required: False
        type: list
        elements: dict
    workers_info:
        description:
            - The IDs of the worker node
        required: False
        type: list
        elements: dict
    kube_version:
        description:
            - Kubernetes version info
        required: False
        type: str
    gateway_enabled:
        description:
            - Set true for gateway enabled clusters
        required: False
        type: bool
        default: False
    hardware:
        description:
            - (Required for new resource) Hardware type
        required: True
        type: str
    force_delete_storage:
        description:
            - Force the removal of a cluster and its persistent storage. Deleted data cannot be recovered
        required: False
        type: bool
        default: False
    private_service_endpoint:
        description:
            - None
        required: False
        type: bool
    disk_encryption:
        description:
            - disc encryption done, if set to true.
        required: False
        type: bool
        default: True
    private_vlan_id:
        description:
            - Private VLAN ID
        required: False
        type: str
    machine_type:
        description:
            - Machine type
        required: False
        type: str
    pod_subnet:
        description:
            - Custom subnet CIDR to provide private IP addresses for pods
        required: False
        type: str
    id:
        description:
            - (Required when updating or destroying existing resource) IBM Cloud Resource ID.
        required: False
        type: str
    state:
        description:
            - State of resource
        choices:
            - available
            - absent
        default: available
        required: False
    ibmcloud_api_key:
        description:
            - The IBM Cloud API key to authenticate with the IBM Cloud
              platform. This can also be provided via the environment
              variable 'IC_API_KEY'.
        required: True

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('name', 'str'),
    ('datacenter', 'str'),
    ('hardware', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'public_vlan_id',
    'service_subnet',
    'resource_group_id',
    'tags',
    'subnet_id',
    'default_pool_size',
    'labels',
    'wait_for_worker_update',
    'wait_till',
    'no_subnet',
    'patch_version',
    'update_all_workers',
    'entitlement',
    'name',
    'public_service_endpoint',
    'webhook',
    'datacenter',
    'kms_config',
    'workers_info',
    'kube_version',
    'gateway_enabled',
    'hardware',
    'force_delete_storage',
    'private_service_endpoint',
    'disk_encryption',
    'private_vlan_id',
    'machine_type',
    'pod_subnet',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
    'cluster_name_id',
    'resource_group_id',
    'space_guid',
    'list_bounded_services',
    'region',
    'alb_type',
    'org_guid',
    'name',
    'account_guid',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    public_vlan_id=dict(
        required=False,
        type='str'),
    service_subnet=dict(
        required=False,
        type='str'),
    resource_group_id=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    subnet_id=dict(
        required=False,
        elements='',
        type='list'),
    default_pool_size=dict(
        required=False,
        type='int'),
    labels=dict(
        required=False,
        elements='',
        type='dict'),
    wait_for_worker_update=dict(
        required=False,
        type='bool'),
    wait_till=dict(
        required=False,
        type='str'),
    no_subnet=dict(
        required=False,
        type='bool'),
    patch_version=dict(
        required=False,
        type='str'),
    update_all_workers=dict(
        required=False,
        type='bool'),
    entitlement=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    public_service_endpoint=dict(
        required=False,
        type='bool'),
    webhook=dict(
        required=False,
        elements='',
        type='list'),
    datacenter=dict(
        required=False,
        type='str'),
    kms_config=dict(
        required=False,
        elements='',
        type='list'),
    workers_info=dict(
        required=False,
        elements='',
        type='list'),
    kube_version=dict(
        required=False,
        type='str'),
    gateway_enabled=dict(
        required=False,
        type='bool'),
    hardware=dict(
        required=False,
        type='str'),
    force_delete_storage=dict(
        required=False,
        type='bool'),
    private_service_endpoint=dict(
        required=False,
        type='bool'),
    disk_encryption=dict(
        required=False,
        type='bool'),
    private_vlan_id=dict(
        required=False,
        type='str'),
    machine_type=dict(
        required=False,
        type='str'),
    pod_subnet=dict(
        required=False,
        type='str'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True)
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    conflicts = {}
    if len(TL_CONFLICTS_MAP) != 0:
        for arg in TL_CONFLICTS_MAP:
            if module.params[arg]:
                for conflict in TL_CONFLICTS_MAP[arg]:
                    try:
                        if module.params[conflict]:
                            conflicts[arg] = conflict
                    except KeyError:
                        pass
    if len(conflicts):
        module.fail_json(msg=("conflicts exist: {}".format(conflicts)))

    result_ds = ibmcloud_terraform(
        resource_type='ibm_container_cluster',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.23.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_container_cluster',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.23.0',
            tl_required_params=TL_REQUIRED_PARAMETERS,
            tl_all_params=TL_ALL_PARAMETERS)
        if result['rc'] > 0:
            module.fail_json(
                msg=Terraform.parse_stderr(result['stderr']), **result)

        module.exit_json(**result)
    else:
        module.exit_json(**result_ds)


def main():
    run_module()


if __name__ == '__main__':
    main()
