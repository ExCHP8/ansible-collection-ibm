#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_container_alb_cert
short_description: Configure IBM Cloud 'ibm_container_alb_cert' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_container_alb_cert' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.3.0
    - Terraform v0.12.20

options:
    domain_name:
        description:
            - None
        required: False
        type: str
    cloud_cert_instance_id:
        description:
            - None
        required: False
        type: str
    region:
        description:
            - None
        required: False
        type: str
    cert_crn:
        description:
            - (Required for new resource) 
        required: False
        type: str
    secret_name:
        description:
            - (Required for new resource) 
        required: False
        type: str
    expires_on:
        description:
            - None
        required: False
        type: str
    issuer_name:
        description:
            - None
        required: False
        type: str
    cluster_crn:
        description:
            - None
        required: False
        type: str
    cluster_id:
        description:
            - (Required for new resource) 
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
            - The API Key used for authentification. This can also be
              provided via the environment variable 'IC_API_KEY'.
        required: True
    ibmcloud_region:
        description:
            - Denotes which IBM Cloud region to connect to
        default: us-south
        required: False
    ibmcloud_zone:
        description:
            - Denotes which IBM Cloud zone to connect to in multizone
              environment. This can also be provided via the environmental
              variable 'IC_ZONE'.
        required: False

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('cert_crn', 'str'),
    ('secret_name', 'str'),
    ('cluster_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'domain_name',
    'cloud_cert_instance_id',
    'region',
    'cert_crn',
    'secret_name',
    'expires_on',
    'issuer_name',
    'cluster_crn',
    'cluster_id',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    domain_name=dict(
        required=False,
        type='str'),
    cloud_cert_instance_id=dict(
        required=False,
        type='str'),
    region=dict(
        required=False,
        type='str'),
    cert_crn=dict(
        required=False,
        type='str'),
    secret_name=dict(
        required=False,
        type='str'),
    expires_on=dict(
        required=False,
        type='str'),
    issuer_name=dict(
        required=False,
        type='str'),
    cluster_crn=dict(
        required=False,
        type='str'),
    cluster_id=dict(
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
        required=True),
    ibmcloud_region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_zone=dict(
        type='str',
        fallback=(env_fallback, ['IC_ZONE']))
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.ibmcloud as ibmcloud

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

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_container_alb_cert',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.3.0',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=ibmcloud.Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
