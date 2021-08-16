#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_cis_cache_settings
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cis_cache_settings

short_description: Configure IBM Cloud 'ibm_cis_cache_settings' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cis_cache_settings' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.29.0
    - Terraform v0.12.20

options:
    caching_level:
        description:
            - Cache level setting
        required: False
        type: str
    serve_stale_content:
        description:
            - Serve Stale Content
        required: False
        type: str
        default: on
    browser_expiration:
        description:
            - Browser Expiration setting
        required: False
        type: int
    query_string_sort:
        description:
            - Query String sort setting
        required: False
        type: str
    purge_by_urls:
        description:
            - Purge by URLs
        required: False
        type: list
        elements: str
    cis_id:
        description:
            - (Required for new resource) CIS instance crn
        required: True
        type: str
    domain_id:
        description:
            - (Required for new resource) Associated CIS domain
        required: True
        type: str
    development_mode:
        description:
            - Development mode setting
        required: False
        type: str
    purge_all:
        description:
            - Purge all setting
        required: False
        type: bool
    purge_by_tags:
        description:
            - Purge by tags
        required: False
        type: list
        elements: str
    purge_by_hosts:
        description:
            - Purge by hosts
        required: False
        type: list
        elements: str
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
    iaas_classic_username:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure (SoftLayer) user name. This can also be provided
              via the environment variable 'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure API key. This can also be provided via the
              environment variable 'IAAS_CLASSIC_API_KEY'.
        required: False
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
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
    ('cis_id', 'str'),
    ('domain_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'caching_level',
    'serve_stale_content',
    'browser_expiration',
    'query_string_sort',
    'purge_by_urls',
    'cis_id',
    'domain_id',
    'development_mode',
    'purge_all',
    'purge_by_tags',
    'purge_by_hosts',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('cis_id', 'str'),
    ('domain_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'cis_id',
    'domain_id',
]

TL_CONFLICTS_MAP = {
    'purge_by_urls': ['purge_all', 'purge_by_tags', 'purge_by_hosts'],
    'purge_all': ['purge_by_urls', 'purge_by_tags', 'purge_by_hosts'],
    'purge_by_tags': ['purge_all', 'purge_by_urls', 'purge_by_hosts'],
    'purge_by_hosts': ['purge_all', 'purge_by_urls', 'purge_by_tags'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    caching_level=dict(
        required=False,
        type='str'),
    serve_stale_content=dict(
        required=False,
        type='str'),
    browser_expiration=dict(
        required=False,
        type='int'),
    query_string_sort=dict(
        required=False,
        type='str'),
    purge_by_urls=dict(
        required=False,
        elements='',
        type='list'),
    cis_id=dict(
        required=False,
        type='str'),
    domain_id=dict(
        required=False,
        type='str'),
    development_mode=dict(
        required=False,
        type='str'),
    purge_all=dict(
        required=False,
        type='bool'),
    purge_by_tags=dict(
        required=False,
        elements='',
        type='list'),
    purge_by_hosts=dict(
        required=False,
        elements='',
        type='list'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
    iaas_classic_username=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_USERNAME']),
        required=False),
    iaas_classic_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_API_KEY']),
        required=False),
    region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
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
        resource_type='ibm_cis_cache_settings',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.29.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_cis_cache_settings',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.29.0',
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
